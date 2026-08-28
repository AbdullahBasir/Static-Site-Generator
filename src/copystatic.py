import shutil
import os

def copy_files(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
            print(f"Copied: {from_path} To: {dest_path}")
        else:
            copy_files(from_path, dest_path)

def static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_files(source, destination)