import pathlib
import zipfile


def extract_archive(filepath, dest_folder):
    folder = pathlib.Path(dest_folder, 'NewFolder')
    with zipfile.ZipFile(filepath, 'r') as extracted:
        extracted.extractall(folder)


''' This is to test if the function is working fine or not 
we can give two files(zipfile and folder) within Bonus_Apps project to test the function '''

# if __name__ == '__main__':
#     extract_archive()
