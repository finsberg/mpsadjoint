# -*- coding: utf-8 -*-
"""

Åshild Telle / Simula Research Laboratory / 2020

"""

from __future__ import print_function

import os
import sys
import platform
import glob

from setuptools import setup, find_packages

if sys.version_info < (3, 5):
    print("Python 3.5 or higher required, please upgrade.")
    sys.exit(1)


def run_install():
    setup(
        name="mpsadjoint",
        description="Software",
        version="0.1",
        author="Åshild Telle",
        license="MIT",
        author_email="aashild@simula.no",
        platforms=["Linux"],
        packages=find_packages("."),
        package_dir={"mpsadjoint": "mpsadjoint"},
        install_requires=[],
        zip_safe=False,
    )


if __name__ == "__main__":
    run_install()
