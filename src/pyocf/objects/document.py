"""Object describing a document"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/objects/Document.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.types.md5 import Md5
from pyocf.types.objectreference import ObjectReference
from typing import Annotated
from typing import Literal
from typing import Optional


class Document(Object):
    """Object describing a document"""

    object_type: Annotated[Literal["DOCUMENT"], Field(description="")] = "DOCUMENT"
    path: Optional[
        Annotated[
            str,
            Field(
                description="Relative path/filename for the document. Path is understood to be a relative"
                "location within an associated ZIP archive (packaged separately from the OCF"
                "archive) e.g. './acceptance_records/John_Wayne_2017_Grant_Agreement.pdf'"
            ),
        ]
    ] = None
    related_objects: Optional[
        Annotated[
            list[ObjectReference],
            Field(description="List of objects which this document is related to"),
        ]
    ] = None
    uri: Optional[
        Annotated[
            str,
            Field(
                description="Uniform resource identifier for the document if not using the `path` property"
                "and associated ZIP archive separate from the OCF package."
            ),
        ]
    ] = None
    md5: Annotated[Md5, Field(description="MD5 file checksum")]
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
