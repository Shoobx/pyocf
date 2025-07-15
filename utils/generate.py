import json
import pathlib
import re
import textwrap

from collections import defaultdict
from collections.abc import Mapping
from mako.template import Template

IDENTIFIER_RE = re.compile("[^0-9a-zA-Z_]")

PROPERTY_TYPES_MAP = {
    "string": "str",
    "array": "list",
    "integer": "int",
    "boolean": "bool",
    "null": "None",
}
# Schema object storage
all_schemas = {}
all_aliases = {}
all_types = {}


def multilinewrap(text):
    # Black doesn't wrap comments, so we have to.
    # But that's the easy bit anyway. We let Black handle the code formatting.
    result = []
    for line in text.splitlines():
        line = line.replace('"', '\\"').replace("'", "\\'")
        result.extend(textwrap.wrap(line, 80))

    return result


class Reference:
    def __init__(self, refid):
        self.refid = refid

    def resolve(self):
        return all_schemas[self.refid]

    @property
    def import_statement(self):
        return self.resolve().import_statement

    def __hash__(self):
        return hash(self.refid)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.refid == other.refid

    def __repr__(self):
        return f"<Reference {self.import_statement}>"


class Property:
    def __init__(self, name, json, schema, required):
        self.name = name
        self.json = json
        self.schema = schema
        self.required = required

    @property
    def python_type(self):
        if "type" in self.json:
            type_ = self.get_python_type(self.json["type"])

        elif "const" in self.json:
            type_ = f'Literal["{self.json["const"]}"]'

        elif "$ref" in self.json:
            type_ = self.json["$ref"].resolve().name

        elif "oneOf" in self.json:
            type_ = f"{self.get_python_type(self.json['oneOf'])}"

        elif "enum" in self.json:
            # This is an enum without the "const", which happens for the type,
            # in cases with backwards compatibilities.
            print(
                f"Warning: In {self.schema.path} the {self.name} property is an enum "
                f"without a const. This should be a Literal, pick the last one."
            )
            type_ = f'Literal["{self.json["enum"][-1]}"]'

        if type_ == "str" and "pattern" in self.json:
            return f"""constr(pattern=r"{self.json['pattern']}")"""

        return type_

    def get_python_type(self, type_):
        if isinstance(type_, Reference):
            return type_.resolve().name

        if isinstance(type_, list):
            types = []
            for t in type_:
                if "$ref" in t:
                    types.append(self.get_python_type(t["$ref"]))
                elif "type" in t:
                    types.append(self.get_python_type(t["type"]))
            if len(types) > 1:
                # I need to check this, because if there is a oneOf of just one type,
                # if you also have a discriminator, you get an error.
                subtype = ", ".join(types)
                return f"Union[{subtype}]"
            # It's a union of one, just return the one.
            return types[0]

        return PROPERTY_TYPES_MAP[type_]

    @property
    def description(self):
        desc = "'\n         '".join(multilinewrap(self.json.get("description", "")))
        return f"{desc}"

    def get_discriminator(self, json):
        if "anyOf" in json:
            # Pick the last one, because the first one can be null
            subschema = json["anyOf"][-1]["$ref"].resolve()
        elif "oneOf" in json:
            # Pick the last one, because the first one can be null
            subschema = json["oneOf"][-1]["$ref"].resolve()
        elif "items" in json:
            return self.get_discriminator(json["items"])
        else:
            return None

        for discriminator in ("file_type", "object_type", "type"):
            if discriminator in subschema.json.get("properties", {}):
                return discriminator

    @property
    def definition(self):
        type_ = self.python_type
        subtype = None
        discriminator = None

        if type_ == "list":
            items = self.json["items"]
            if "type" in items:
                subtype = self.get_python_type(items["type"])
            elif "$ref" in items or "type" in items:
                subtype = self.get_python_type(items["$ref"])
            elif "anyOf" in items:
                types = []
                for t in items["anyOf"]:
                    r = t["$ref"]
                    types.append(self.get_python_type(r))
                subtype = f"""Union[{", ".join(types)}]"""

            elif "oneOf" in items:
                types = []
                for t in items["oneOf"]:
                    r = t["$ref"]
                    types.append(self.get_python_type(r))
                    schema = r.resolve()
                    if schema.aliases:
                        types.extend(all_types[x].name for x in schema.aliases)
                subtype = f"""Union[{", ".join(types)}]"""

            discriminator = self.get_discriminator(items)
            if discriminator is not None:
                subtype = (
                    f"Annotated[{subtype}, " f"Field(discriminator='{discriminator}')]"
                )

        if subtype:
            type_ = f"{type_}[{subtype}]"

        if type_.startswith("Union["):
            discriminator = self.get_discriminator(self.json)
            if discriminator is not None:
                type_ = (
                    f"Annotated[{type_}, "
                    f"Field(discriminator='{discriminator}', description='{self.description}')]"
                )
        else:
            type_ = f"Annotated[{type_}, " f"Field(description='{self.description}')]"

        if not self.required and "const" not in self.json:
            type_ = f"Optional[{type_}] = None"

        type_ = f"{self.name}: {type_}"

        if "Literal" in type_:
            if "const" in self.json:
                type_ += f' = "{self.json["const"]}"'
            else:
                type_ += f' = "{self.json["enum"][-1]}"'

        return type_


class Schema:
    """A wrapper around a jsonschema"""

    def __init__(self, path, json):
        self.path = path
        self.name = path.parts[-1].split(".", 1)[0]
        self.filename = self.name.lower()
        if self.name == "File":
            # The name "File" is used by both a primitive and a type,
            # so to avoid a naming conflict, we rename the primitive.
            if "primitives" in path.parts:
                self.name = "FileObject"

        self.json = json
        self.id = json["$id"]

        self._references = set()
        self.dereference_all(self.json)
        self.aliases = []

    def dereference_all(self, json_value):
        if not isinstance(json_value, Mapping):
            return json_value

        for key, val in json_value.items():
            if key == "$ref":
                if isinstance(val, Reference):
                    # Already dereferenced
                    continue
                ref = Reference(val)
                json_value[key] = ref
                self._references.add(ref)
            elif isinstance(val, Mapping):
                self.dereference_all(val)
            elif isinstance(val, list):
                json_value[key] = [self.dereference_all(x) for x in val]

        return json_value

    def __repr__(self):
        return f"<Schema {self.id}>"

    @property
    def metatype(self):
        if "enum" in self.json:
            return "enum"
        if "type" not in self.json:
            print(
                f"Warning: {self.path} doesn't have a type field. Defaulting to 'object' type."
            )
            return "object"
        if self.json["type"] == "string":
            # This is a string with restrictions, currenly we ignore the
            # restrictions, and just make a string subclass
            return "object"

        return self.json["type"]

    @property
    def object_type(self):
        for prop in ("file_type", "object_type", "type"):
            if prop in self.json.get("properties", {}):
                if "enum" in self.json["properties"][prop]:
                    return tuple(self.json["properties"][prop]["enum"])
                elif "const" in self.json["properties"][prop]:
                    return self.json["properties"][prop]["const"]
                print(self.json["properties"])

        return None

    @property
    def description(self):
        return "\n".join(multilinewrap(self.json["description"]))

    @property
    def comment(self):
        return "\n".join(multilinewrap(self.json["$comment"]))

    @property
    def title(self):
        title = self.json["title"]
        if " - " in title:
            title = title.split(" - ", 1)[1]
        title.replace(self.metatype.capitalize(), "")
        return title

    @property
    def superclasses(self):
        if "allOf" in self.json:
            return [x["$ref"].resolve() for x in self.json["allOf"]]
        if self.name == "Numeric" or "format" in self.json or "pattern" in self.json:
            return ["SimpleBaseModel"]
        return ["BaseModel"]

    @property
    def superclass_string(self):
        classes = []
        for cls in self.superclasses:
            if isinstance(cls, Schema):
                classes.append(cls.name)
            else:
                classes.append(cls)

        return ", ".join(classes)

    @property
    def required_properties(self):
        required = set(self.json.get("required", []))
        for superclass in self.superclasses:
            if isinstance(superclass, Schema):
                required.update(superclass.required_properties)
        return required

    @property
    def properties(self):
        if "properties" not in self.json:
            return
        required = self.required_properties
        for name, prop in self.json["properties"].items():
            if prop:
                yield Property(name, prop, self, name in required)
            else:
                yield self._get_super_property(name)

    def _get_super_property(self, name):
        for superclass in self.superclasses:
            for prop in superclass.properties:
                if name == prop.name:
                    return prop

    @property
    def enum(self):
        if "enum" not in self.json:
            return
        for enum in self.json["enum"]:
            # Some OCF enums start with numbers, and/or contain periods.
            # Python doesn't allow that for identifiers:
            name = "ENUM_" + IDENTIFIER_RE.sub("", enum)
            yield name, enum

    def _get_imports_from_json(self, json):
        imports = set()

        if "$ref" in json:
            imports.add(json["$ref"].import_statement)
            if json["$ref"].resolve().aliases:
                imports.update(
                    [
                        all_types[alias].import_statement
                        for alias in json["$ref"].resolve().aliases
                    ]
                )
        elif "oneOf" in json:
            for j in json["oneOf"]:
                imports.update(self._get_imports_from_json(j))
        elif "anyOf" in json:
            for j in json["anyOf"]:
                imports.update(self._get_imports_from_json(j))
        elif "items" in json:
            imports.update(self._get_imports_from_json(json["items"]))

        return imports

    @property
    def import_statements(self):
        """The import statements this schema needs"""
        imports = set()

        for prop in self.properties:
            imports.update(self._get_imports_from_json(prop.json))
            if "Literal" in prop.definition:
                imports.add("from typing import Literal")
            if "Optional" in prop.definition:
                imports.add("from typing import Optional")
            if "Union" in prop.definition:
                imports.add("from typing import Union")
            if "Annotated" in prop.definition:
                imports.add("from typing import Annotated")
            if "Field" in prop.definition:
                imports.add("from pydantic import Field")
            if "constr" in prop.definition:
                imports.add("from pydantic import constr")

        for superclass in self.superclasses:
            if isinstance(superclass, Schema):
                imports.add(superclass.import_statement)
            elif superclass == "BaseModel":
                imports.add("from pydantic import BaseModel")
            elif superclass == "SimpleBaseModel":
                imports.add("from pyocf.simplebase import SimpleBaseModel")

        if self.root_constraint:
            if "constr" in self.root_constraint:
                imports.add("from pydantic import constr")
            if "date" in self.root_constraint:
                imports.add("from datetime import date")
            if "Decimal" in self.root_constraint:
                imports.add("from decimal import Decimal")

        return sorted(imports)

    @property
    def import_statement(self):
        """The import statement to this schema"""
        root = self.path.parts.index("schema") + 1
        path = ("pyocf",) + self.path.parts[root:]
        pkg = ".".join(path[:-1])
        module = self.filename.split(".")[0]
        imp = f"from {pkg}.{module} import {self.name}"
        return imp

    @property
    def root_constraint(self):
        if "format" in self.json:
            return self.json["format"]
        if self.name == "Numeric":
            return "Decimal"

        if "pattern" in self.json:
            return f"""constr(pattern=r"{self.json.get("pattern")}")"""

        return None


def load_schemas(path):
    # Load all schemas
    for directory in pathlib.Path(path).rglob("*.schema.json"):
        print(f"importing {directory}")
        schema = Schema(directory, json.loads(directory.read_text("utf8")))
        print(f"found {schema.name}")
        all_schemas[schema.id] = schema

    # Now make the type mapping:
    for schema in all_schemas.values():
        all_types[schema.object_type] = schema

    return all_schemas


def make_inits(path, types):
    for filepath in path.iterdir():
        if filepath.name.startswith("_"):
            continue
        if filepath.is_dir():
            make_inits(filepath, types)
        elif not filepath.name.endswith(".py"):
            continue

    folder_dupe = pathlib.Path(path.parent, path.name + ".py")
    if folder_dupe.exists():
        # Move it
        target = pathlib.Path(path, "__init__.py")
        folder_dupe.replace(target)
    else:
        with pathlib.Path(path, "__init__.py").open("wt", encoding="utf-8") as initfile:
            initfile.write(f'"""OCF {path.parts[-1]}"""')


def generate_files():
    templdir = pathlib.Path(__file__).parent
    outdir = pathlib.Path(templdir.parent, "src/pyocf")
    types = defaultdict(dict)
    roottypes = defaultdict(dict)
    all_classes = {}

    # Firs look for backwards compatibility classes
    for type_, schema in all_types.items():
        if type_ is None:
            continue
        if isinstance(type_, tuple):
            # Find the new main type
            main_type = None
            for bbb_type in type_:
                if bbb_type not in all_types:
                    # This is the main type, actually
                    main_type = bbb_type
                    break
            del schema.json["properties"]["object_type"]["enum"]
            schema.json["properties"]["object_type"]["const"] = main_type

            for bbb_type in type_:
                if bbb_type != main_type:
                    # This is a bbb type
                    all_aliases[bbb_type] = schema
                    schema.aliases.append(bbb_type)

    for schema in all_schemas.values():
        rootlevel = schema.path.parts.index("schema") + 1
        schema_dir = pathlib.Path(*schema.path.parts[rootlevel:-1])
        object_type = schema.object_type
        if object_type is not None:
            types[pathlib.Path(outdir, schema_dir)][object_type] = schema
            roottypes[object_type] = schema
        tmpl = Template(filename=f"{templdir}/{schema.metatype}.mako")
        path = pathlib.Path(schema_dir, schema.filename + ".py")
        outfile = pathlib.Path(outdir, path)
        outfile.parent.mkdir(parents=True, exist_ok=True)
        with outfile.open("wt", encoding="utf-8") as outfile:
            outfile.write(tmpl.render(schema=schema))
        if schema.name in all_classes:
            raise ValueError(
                "The schema has changed to include duplicate class names, "
                "that's new and needs dealing with!"
            )
        all_classes[schema.name] = schema.import_statement

    classes_file = pathlib.Path(outdir, "api.py")
    with classes_file.open("wt", encoding="utf-8") as outfile:
        outfile.write('"""All PyOCF classes, for easier import"""\n\n')
        outfile.write("# Autogenerated, do not edit.\n# Copyright © 2023 FMR LLC\n\n")

        for imports in sorted(all_classes.values()):
            outfile.write(f"{imports}\n")

        outfile.write(f"\n__all__ = [{', '.join(sorted(all_classes))}]")

    make_inits(outdir, types)


if __name__ == "__main__":
    load_schemas("./Open-Cap-Format-OCF/schema")
    generate_files()
