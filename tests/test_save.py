# Copyright © 2023 FMR LLC

import tempfile
import zipfile

from pathlib import Path

from pyocf.captable import Captable

sample_path = Path(Path(__file__).parent.parent, "Open-Cap-Format-OCF/samples")


def test_save_zip():
    path = Path(Path(__file__).parent, "samples/Captable.ocf.zip")
    captable = Captable.load(path)

    try:
        with tempfile.TemporaryDirectory() as outdir:
            outpath = Path(outdir, "outfile.zip")

            captable.save(outpath, pretty=True)
            with zipfile.ZipFile(outpath) as zipped:
                assert len(zipped.filelist) == 8
                # Make sure the manifest file is in there
                assert zipped.filelist[7].filename == "Manifest.ocf.json"

                manifest = zipped.open("Manifest.ocf.json")
                data = manifest.read()

                # Do some simple checks on the data
                assert b'"file_type": "OCF_MANIFEST_FILE"' in data
                assert b'"filepath": "StockLegends.ocf.json",' in data

            outpath.unlink()

    except (PermissionError, NotADirectoryError):
        # Bugs in windows give permission errors for absolutely no reason
        # when deleting temporary files. Ignore them.
        pass


def test_save_directory():
    path = Path(Path(__file__).parent, "samples/Captable.ocf.zip")
    captable = Captable.load(path)

    try:
        with tempfile.TemporaryDirectory() as outdir:
            captable.save(outdir, zip=False, pretty=True)

            path = Path(outdir)
            files = [x for x in path.iterdir()]
            assert len(files) == 8
            # Make sure the manifest file is in there
            manifest = [x for x in files if x.name == "Manifest.ocf.json"][0]
            data = manifest.open("rb").read()

            # Do some simple checks on the data
            assert b'"file_type": "OCF_MANIFEST_FILE"' in data
            assert b'"filepath": "StockLegends.ocf.json",' in data
    except (PermissionError, NotADirectoryError):
        # Bugs in windows give permission errors for absolutely no reason
        # when deleting temporary files. Ignore them.
        pass
