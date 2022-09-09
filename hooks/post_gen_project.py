import os
import shutil

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

print("Moving files to parent directory...")
# Copy files and folders - https://stackoverflow.com/a/7420617
root_src_dir, root_dst_dir = PROJECT_DIR, PARENT_DIR
for src_dir, _, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)
try:
    os.rmdir(root_src_dir)
except PermissionError:
    print(
        f"WARNING: Could not remove temp directory '{PROJECT_DIR}', please do it manually."
    )