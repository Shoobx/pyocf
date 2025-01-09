"""OCF Captable object"""

# Copyright © 2023 FMR LLC

import datetime
import hashlib
import json
import pathlib
import zipfile

from pyocf.files import ocfmanifestfile
from pyocf.files import stakeholdersfile
from pyocf.files import stockclassesfile
from pyocf.files import stocklegendtemplatesfile
from pyocf.files import stockplansfile
from pyocf.files import transactionsfile
from pyocf.files import valuationsfile
from pyocf.files import vestingtermsfile
from pyocf.objects.stakeholder import Stakeholder
from pyocf.objects.stockclass import StockClass
from pyocf.objects.stocklegendtemplate import StockLegendTemplate
from pyocf.objects.stockplan import StockPlan
from pyocf.objects.valuation import Valuation
from pyocf.objects.vestingterms import VestingTerms
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types import file

FILEMAP = [
    ("stock_plans", stockplansfile.StockPlansFile),
    ("stock_legend_templates", stocklegendtemplatesfile.StockLegendTemplatesFile),
    ("stock_classes", stockclassesfile.StockClassesFile),
    ("vesting_terms", vestingtermsfile.VestingTermsFile),
    ("valuations", valuationsfile.ValuationsFile),
    ("transactions", transactionsfile.TransactionsFile),
    ("stakeholders", stakeholdersfile.StakeholdersFile),
]


class Captable:
    manifest: ocfmanifestfile.OCFManifestFile = None
    stock_plans: list[StockPlan] = []
    stock_legend_templates: list[StockLegendTemplate] = []
    stock_classes: list[StockClass] = []
    vesting_terms: list[VestingTerms] = []
    valuations: list[Valuation] = []
    transactions: list[Transaction] = []
    stakeholders: list[Stakeholder] = []

    @classmethod
    def load(cls, location):
        """Imports OCF data

        `location` needs to be a string or a pathlib.Path() pointing at a
        zipfile or directory containing the OCF files, or it must be a
        file-like object containing a zip-file.
        """
        captable = Captable()

        # Assume it's a zip file or path to a zip file
        try:
            inzipfile = zipfile.ZipFile(location)
            manifest = json.loads(inzipfile.read("Manifest.ocf.json"))
            captable.manifest = ocfmanifestfile.OCFManifestFile(**manifest)

            def file_factory(p):
                # Normalize the path:
                p = str(pathlib.Path(p))
                return inzipfile.open(p)

        except zipfile.BadZipfile:
            # OK, then, let's assume it's a Manifest file in a directory

            # Make sure it's a pathlib path
            path = pathlib.Path(location)

            with path.open("rt") as infile:
                manifest = json.load(infile)
                captable.manifest = ocfmanifestfile.OCFManifestFile(**manifest)
                basedir = path.parent

            def file_factory(p):
                return open(pathlib.Path(basedir, p))

        for filetype, filecls in FILEMAP:
            for fileob in getattr(captable.manifest, filetype + "_files"):
                infile = file_factory(fileob.filepath)
                items = filecls(**json.load(infile)).items
                getattr(captable, filetype).extend(items)

        return captable

    def _save_ocf_files(self, manifest_path, issuer, file_factory, pretty):
        if issuer is None and self.manifest is None:
            raise ValueError(
                "You must specify an issuer, either by passing the value to the"
                "save method, or by creating a Manifest."
            )

        manifest_data = {}
        for filetype, fileob in FILEMAP:
            # Set the filename:
            ocffilename = filetype + ".ocf.json"

            if self.manifest:
                # Check if there is a different filename in the manifest:
                ocffilename = getattr(self.manifest, filetype + "_files", [])
                if len(ocffilename) >= 1:
                    ocffilename = ocffilename[0].filepath

            # Normalize the path
            ocffilename = str(pathlib.Path(ocffilename))

            with file_factory(ocffilename) as ocffile:
                itemfile = fileob(items=getattr(self, filetype))
                jsonstr = itemfile.json(exclude_unset=True)
                if pretty:
                    jsonstr = json.dumps(json.loads(jsonstr), indent=4)
                jsonstr = jsonstr.encode("UTF-8")
                md5 = hashlib.md5(jsonstr).hexdigest()
                ocffile.write(jsonstr)
                manifest_data[filetype + "_files"] = [
                    file.File(filepath=ocffilename, md5=md5)
                ]

        if self.manifest is not None:
            manifest_data.update(
                {
                    "issuer": self.manifest.issuer,
                    "as_of": self.manifest.as_of,
                    "generated_at": self.manifest.generated_at,
                    "comments": self.manifest.comments,
                }
            )
        else:
            manifest_data.update(
                {
                    "issuer": issuer,
                    "as_of": datetime.date.today(),
                    "generated_at": datetime.datetime.now().isoformat(),
                }
            )

        self.manifest = ocfmanifestfile.OCFManifestFile(**manifest_data)

        with file_factory(manifest_path) as ocffile:
            jsonstr = self.manifest.json()
            if pretty:
                jsonstr = json.dumps(json.loads(jsonstr), indent=4)
            ocffile.write(jsonstr.encode("UTF-8"))

    def save(
        self,
        location,
        manifest_path="Manifest.ocf.json",
        issuer=None,
        zip=True,
        pretty=True,
    ):
        """Save the captable to a zipfile or a directory

        For each file type, only one file will be created.
        If several file names are specified only the first one
        will be used.
        """
        if zip:
            # Attempt standard PKZIP deflation
            if zipfile._get_compressor(zipfile.ZIP_DEFLATED) is None:
                # Didn't work, don't compress it
                compression = zipfile.ZIP_STORED
            else:
                compression = zipfile.ZIP_DEFLATED

            with zipfile.ZipFile(
                location, mode="w", compression=compression
            ) as outzipfile:
                self.save_zipfile(outzipfile, manifest_path, issuer, pretty=pretty)

        else:
            path = pathlib.Path(location).absolute()
            # Make sure it exists (and is a directory)
            # This gives good error messages if not a valid directory path
            path.mkdir(exist_ok=True)
            self.save_directory(path, pretty=pretty)

    def save_zipfile(
        self, outzipfile, manifest_path="Manifest.ocf.json", issuer=None, pretty=True
    ):
        """Save to an already open zipfile

        Useful if you require non-standard compression or other zipfile options,
        then you can open the zipfile yourself and use this function to save to it.
        """

        def file_factory(p):
            return outzipfile.open(p, mode="w")

        self._save_ocf_files(manifest_path, issuer, file_factory, pretty)

    def save_directory(
        self, outdirectory, manifest_path="Manifest.ocf.json", issuer=None, pretty=True
    ):
        """Save to a directory"""

        def file_factory(p):
            return open(pathlib.Path(outdirectory, p), mode="wb")

        self._save_ocf_files(manifest_path, issuer, file_factory, pretty)
