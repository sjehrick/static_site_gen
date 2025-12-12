import os
import shutil

def copy_source_dest(source_dir, dest_dir):
    absolute_source = os.path.abspath(source_dir)
    absolute_dest = os.path.abspath(dest_dir)

    shutil.rmtree(absolute_dest, ignore_errors=True)

    os.mkdir(absolute_dest)

