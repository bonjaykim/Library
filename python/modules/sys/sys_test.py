
import sys

def main():
    # argv: is a list in Python, which contains the command-line arguments passed to the script
    print(sys.argv)

    # exit script
    #sys.exit()

    # list of strings that specifies the search path for modules.
    print(sys.path)

    # version
    print(sys.version)

    # stdin, out, error
    #for line in sys.stdin:
    #    print(line)
    sys.stdout.write('This is standard output\n')
    sys.stderr.write('This is standard error\n')

    # the size of an object in bytes
    a = 32
    print(sys.getsizeof(a))

    # check platform name
    print(sys.platform)
    print('win' in sys.platform)

    # gives the path of the Python interpreter binary.
    print(sys.executable)

    # indicates the largest integer a variable can take
    print(sys.maxsize)

    # current default string encoding used by the Unicode implementation
    print(sys.getdefaultencoding())

if __name__ == '__main__':
    main()