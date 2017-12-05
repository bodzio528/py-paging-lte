# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('paginglte/paginglte.py').read(),
    re.M
    ).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "py-paging-lte",
    packages = ["paginglte"],
    entry_points = {
        "console_scripts": ['paginglte = paginglte.paginglte:main']
        },
    version = version,
    description = "Python command line application calculating paging.",
    long_description = long_descr,
    author = "Bogumil Chojnowski",
    author_email = "bogumil.chojnowski@gmail.com",
    url = "https://github.com/bodzio528/py-paging-lte",
    )
