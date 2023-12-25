
import os
import shutil

def get_current_directory():
    return os.getcwd()

def change_directory(directory):
    os.chdir(directory)
    return get_current_directory()

def get_list_files_and_directories(path):
    return os.listdir(path)

def create_new_directory_if_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)

def remove_all_file(path):
    if os.path.isdir(path):
        if not os.listdir(path):
            shutil.rmtree(path)
        else:
            os.rmdir(path)
    elif os.path.isfile(path):
        os.remove(path)

def main():

    # current directory
    current_dir = get_current_directory()
    print(current_dir)

    # Change directory
    print(change_directory(current_dir))

    # List files and directories
    print(get_list_files_and_directories(current_dir))

    # Make a new directory if not exist
    new_dir = "new_dir"
    new_path = os.path.join(current_dir, new_dir)
    create_new_directory_if_not_exist(new_path)
    
    # Rename directory
    # os.rename(current_dir, new_dir)

    # Remove file or directory
    # remove_all_file(path)

    # Get environment variable
    home_directory = os.environ.get('HOME')
    print(home_directory)

    # Set environment variable
    os.environ['PYTHON_OS_TEST_VAR'] = 'value'
    print(os.environ.get('PYTHON_OS_TEST_VAR'))

    # Execute shell script
    os.system('ls -l')

    # Get pid
    pid = os.getpid()
    print(pid)

    # Get full path
    path = os.path.join(get_current_directory(), "os_test.py")
    print(path)

    # Split Path and filename
    directory, filename = os.path.split(path)
    print(directory, " " , filename)

    # Check if path exist
    print(os.path.exists(path))

    # Get file size
    print(os.path.getsize(path))

    # Walking a directory tree
    for root, dirs, files in os.walk(directory):
        print(root)
        print(dirs)
        print(files)

if __name__ == '__main__':
    main()