#! /usr/bin/env python
import os

from setuptools import setup

projectname = "text_cleaner"
exec(open('%s/version.py' % projectname).read())  # loads __version__
with open("README.md", "r") as fh:
    long_description = fh.read()

descr = """Text Cleaner Tools"""

_root = os.path.dirname(os.path.realpath(__file__))
requirements = os.path.join(_root, "requirements.txt")
REQUIREMENTS = [x.strip() for x in open(requirements).readlines()]

if __name__ == "__main__":
    setup(
        name=projectname,
        version=__VERSION__,
        description=descr,
        long_description=long_description,
        install_requires=REQUIREMENTS,
        packages=[projectname],
    )
