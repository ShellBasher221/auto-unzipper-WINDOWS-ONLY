import os
from time import sleep
from pathlib import Path
import importlib.util

def verify_modules() -> None:
    dependacies = ['winshell', 'zipfile', 'tarfile', 'rarfile']
    
    for module in dependacies:
        if importlib.util.find_spec(module) is None:
            print(f"{module} not installed. Intsalling")
            os.system(f"pip install {module}")
        else:
            print(f"{module} is installed")
    print("all dependancies are installed")

def empty_bin() -> None:
    from winshell import recycle_bin
    try:
        recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Recycling bin is now empty.")
    except:
        print("Recycling bin is already empty.")


DOWNLOADS_DIR = Path.home() / 'Downloads'

def fetch_and_unzip_archives() -> None:

    import zipfile
    import tarfile
    import rarfile

    DOWNLOADS_DIR = Path.home() / 'Downloads'
    outfile_name = "unzipped_archives"
    
    if os.path.exists(os.path.join(DOWNLOADS_DIR, outfile_name)):
        outfile = os.path.join(DOWNLOADS_DIR, outfile_name)
        print("unzipped_archives directory found at ", outfile)
    else:
        print("unzipped_archive directory not found. directory is being created in downloads directory...")
        os.mkdir(os.path.join(DOWNLOADS_DIR, outfile_name)) 
        outfile = os.path.join(DOWNLOADS_DIR, outfile_name)
        print("unzipped_archive directory has been made...")

    for file in os.listdir(DOWNLOADS_DIR):

        try:

            if file.endswith(".zip"):

                file = os.path.join(DOWNLOADS_DIR, file)
                with zipfile.ZipFile(file, 'r') as zip_archive:
                    zip_archive.extractall(outfile)           
                    sleep(1)

            if file.endswith(".rar"):

                file = os.path.join(DOWNLOADS_DIR, file)
                with rarfile.RarFile(file, 'r') as rar_archive:
                    rar_archive.extractall(outfile)
                    sleep(1)

            if file.endswith(".tar.gz"):

                os.path.join(DOWNLOADS_DIR, file)
                with tarfile.open(file, 'r:gz') as tar_archive:
                    tar_archive.extractall(outfile)
                    sleep(1)

        except zipfile.BadZipFile or rarfile.BadRarFile or tarfile.TarError:
            print("an archive may be corrupted or not an archive.")

    for file in os.listdir(DOWNLOADS_DIR):
        if file.endswith(".zip") or file.endswith(".rar") or file.endswith(".tar.gz"):

            file = os.path.join(DOWNLOADS_DIR, file)
            os.remove(file)


    print("All archive files in downloads have been unzipped and moved to ", outfile)

def extract_clean() -> None:
    print("WORKING...")
    fetch_and_unzip_archives()
    print("moving original archive files to the recycling bin...")
    empty_bin()


def main() -> None:
    running = True
    while running:
        print("options:\n- extract - will go theough downloads and extract all archive files")
        user_choice = input("--> ")
        if user_choice == "extract":
            verify_modules()
            extract_clean()
            print("operation finished")
            running = False
        else:
            print("Did not enter a valid choice")
            continue

if __name__ == "__main__":
    main()