#
# python jinja_test.py --device name.yaml
#

import os
import argparse
import yaml

from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment

def main():
    parser = argparse.ArgumentParser(description="jinja test")
    parser.add_argument(
        "--device", type=str, required=True, help="path to the device template file"
    )
    parser.add_argument(
        "--path",
        default="./",
        type=str,
        help="path to the device and device-type template"
    )
    args = parser.parse_args()

    env = SandboxedEnvironment(
        loader=FileSystemLoader(
            [
                os.path.join(args.path, "jinja_test_1"),
                os.path.join(args.path, "jinja_test_2")
            ]
        ),
        trim_blocks=True,
        autoescape=False,
    )
    if os.path.exists(
        os.path.join(args.path, "jinja_test_1", "%s.jinja2" % args.device)
    ):
        print("can't find %s device file" % args.device)
    
    template = env.get_template("%s.jinja2" % args.device)
    ctx = {
        "port": 5000,
        "username": "Jaecheol",
        "userpassword": "password",
        "file": "out/test.txt"
    }
    config = template.render(**ctx)

    print("YAML config")
    print("=========================")
    print(config)
    print("=========================")
    print(yaml.safe_load(config))

if __name__ == "__main__":
    main()