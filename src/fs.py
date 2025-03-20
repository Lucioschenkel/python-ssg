import os
import shutil


def cleanup_directory(dir: str):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def create_directory(name: str):
    os.mkdir(name)


def copy_recursive(source: str, dest: str):
    files = os.listdir(source)
    for file in files:
        print(f"processing {file}")
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path):
            if not os.path.exists(dest):
                create_directory(dest)
            shutil.copy(os.path.join(source, file), dest)
        else:
            copy_recursive(os.path.join(source, file), os.path.join(dest, file))
