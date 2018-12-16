import os
from setuptools import setup
from os.path import abspath, join, dirname

if __name__ == '__main__':
    CURDIR = dirname(abspath(__file__))
    with open(join(CURDIR, 'version.py'), 'r') as f:
        version=exec(f.read())
        print(VERSION)