import os
import shutil

def copy_source_dest(source_dir, dest_dir):
    absolute_source = os.path.abspath(source_dir)
    print(f"absolute source is {absolute_source}")
    absolute_dest = os.path.abspath(dest_dir)
    print(f"absolute dest is {absolute_dest}")

    shutil.rmtree(absolute_dest, ignore_errors=True)

    os.mkdir(absolute_dest)

    if os.path.exists(absolute_dest):
        print(f"{absolute_dest} successfully created")

    #dirs = [dir for dir in os.listdir(absolute_source) if os.path.isdir(os.path.join(absolute_source, dir))]

    def recursive_copy(src_directory, dest_directory):
        absolute_dir = os.path.abspath(src_directory)
        #print(absolute_dir)

        files = [file for file in os.listdir(absolute_dir) if os.path.isfile(os.path.join(absolute_dir, file))]

        nested_dirs = [dir for dir in os.listdir(absolute_dir) if os.path.isdir(os.path.join(absolute_dir, dir))]

        for file in files:
            abs_file = os.path.join(absolute_dir, file)
            print(f"Copying {abs_file} to {dest_directory}")
            shutil.copy(abs_file, dest_directory)

        for dir in nested_dirs:

            new_dest = os.path.abspath(os.path.join(dest_directory, dir))
            #print(new_dest)

            
            shutil.rmtree(new_dest, ignore_errors=True)

            os.mkdir(new_dest)
            
            if os.path.exists(new_dest):
                print(f"{new_dest} successfully created")

            abs_dir = os.path.join(absolute_dir, dir)
            #print(abs_dir)

            recursive_copy(abs_dir, new_dest)

    recursive_copy(absolute_source, absolute_dest)

    #for dir in dirs:
     #   recursive_copy(dir)
