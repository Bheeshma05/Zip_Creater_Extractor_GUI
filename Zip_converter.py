import pathlib
import zipfile


def make_archive(filepaths, dest_folder):

    folder = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(folder, 'w') as archive:
        for files in filepaths:
            files = pathlib.Path(files)
            archive.write(files, arcname=files.name)
