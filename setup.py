#!/usr/bin/env python
import sys
from distutils.cmd import Command
from distutils.util import convert_path

from setuptools import setup


def read_long_description(filename="README.rst"):
    with open(filename) as f:
        return f.read().strip()


def read_requirements(filename="requirements.txt"):
    with open(filename) as f:
        return f.readlines()


class PyTest(Command):
    test_args = []
    test_suite = True
    user_options = [("rt", "r", "run_test")]

    def initialize_options(self):
        self.test_args = []
        self.test_suite = True

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


main_ns = {}
ver_path = convert_path('ciarlare/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="ciarlare",
    version=main_ns["__version__"],
    author="Charles-Axel Dein",
    author_email="charles@uber.com",
    license="MIT",
    cmdclass={'test': PyTest},
    url="https://github.com/uber/charlatan",
    packages=["ciarlare"],
    keywords=["tests", "fixtures", "database"],
    description="Efficiently manage and install data fixtures",
    long_description=read_long_description(),
    install_requires=["PyYAML>=3.10", "pytz"] + ['pytest'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9+",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
