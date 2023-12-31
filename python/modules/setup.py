#
# This file currently now working correctly and it was referenced by following link
# : pythonhosted.org/an_example_pypi_project/setuptools.html
# 

import os
import setuptools
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def main():
    print(setuptools.__file__)

    setup(
        name = "Jaecheol Python Test Library",
        version = "0.0.1",
        author = "Jaecheol Kim",
        author_email = "kjc9911@naver.com",
        description = ("An demonstration of how to use python modules"),
        license = "BSD",
        keywords = "example of python module tutorial",
        url = "http://packages.python.org/jay_python_module_test",
        #packages = os.listdir('.'),
        packages = [
            'argparse', 'jinja2'
        ],
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
        ]
    )

if __name__ == '__main__':
    main()