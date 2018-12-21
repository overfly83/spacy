import os
from setuptools import setup, find_packages
from os.path import abspath, join, dirname

CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'version.py'),'r') as f:
    exec(f.read())

DESCRIPTION = """
Integration NLQ technology with SAC system so that user may control
SAC in natural languages via voice control.
"""[1:-1]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open(join(CURDIR, 'REQUIREMENTS.txt')) as f:
    REQUIREMENTS = f.read().splitlines()
print(REQUIREMENTS)
setup(
    name="Spacy integration with SAC",
    version=VERSION,
    author="Edward Zhang",
    author_email="edward.zhang@sap.com",
    description=DESCRIPTION,
    license="MIT",
    url="https://github.com/overfly83/spacy",
    package_dir={'': '.'},
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    platforms='any'
)
