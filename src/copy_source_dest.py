import os
import shutil

def copy_source_dest(source_dir, dest_dir):
    absolute_source = os.path.abspath(source_dir)
    absolute_dest = os.path.abspath(dest_dir)

    shutil.rmtree(absolute_dest, ignore_errors=True)

    os.mkdir(absolute_dest)

    dirs = [dir for dir in os.listdir(absolute_source) if os.path.isdir(os.path.join(absolute_source, dir))]

    def recursive_copy(directory):
        
        absolute_dir = os.path.abspath(directory)

        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(absolute_dir, file))]

        for file in files:
            print(f"Copying {file} to {absolute_dest}")
            shutil.copy(file, absolute_dest)

    recursive_copy(absolute_source)

    for dir in dirs:
        recursive_copy(dir)
