
import os
import sys
import shutil

def main():
    # copy a file 
    shutil.copy("source.txt", "destination.txt")

    # copy an entire directory tree
    if sys.version_info >= (3, 8):
        shutil.copytree('source', 'destination', dirs_exist_ok=True)
    else:
        if os.path.exists('destination'):
            shutil.copytree('source', 'destination')
        else:
            print("Error: destination directory already exists..")

    # remove a directory and its contents
    shutil.rmtree('./destination')

    # move a file or directory
    shutil.move('./source.txt', './move.txt')
    shutil.move('./move.txt', './source.txt')

    # get disk usage statistics
    total, used, free = shutil.disk_usage("./").total, shutil.disk_usage("./").used, shutil.disk_usage("./").free
    print(f'total({total}), used({used}), free({free})')

if __name__ == '__main__':
    main()