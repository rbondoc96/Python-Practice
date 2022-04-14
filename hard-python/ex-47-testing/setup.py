from setuptools import setup, find_packages

from typing import Dict

VERSION = "0.0.1"
DESCRIPTION = "A basic package."

"""
'install_requires' : What packages should be installed when this module is installed
"""
config: Dict[str, str] = {
    "name": "Exercise47",
    "version": VERSION,
    "author": "Rodrigo Bondoc",
    "author_email": "<myemail@email.com>",
    "description": "Exercise 46",
    "url": "URL to get the project at",
    "download_url": "Where to download it",
    "install_requires": [],
    "packages": ["ex47"],   # Want to leave out the tests/ dir
    "scripts": [],
}

setup(**config)