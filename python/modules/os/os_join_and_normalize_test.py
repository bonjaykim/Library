
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("device", type=argparse.FileType('r'), help="device template")
    parser.add_argument(
        "--path", type=str, action="append", help="template lookup path"
    )

    options = parser.parse_args()

    # Set the default path
    if options.path is None:
        options.path = [
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "depth_1",
                "depth_2",
                "depth_3",
            )
        ]
    
    print(options.path)

    # Normalize path
    for path in options.path:
        print(os.path.normpath(path))

if __name__ == '__main__':
    sys.exit(main())