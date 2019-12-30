# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

PACKAGES = ["connectivity"] + ["connectivity.%s" % i for i in find_packages("connectivity")]
PACKAGES = PACKAGES + ["systems"] + ["systems.%s" % i for i in find_packages("systems")]

setup(
    name="pytratto",
    version="0.0.1",
    packages=PACKAGES,
    license="BSD 3-clause",
    install_requires=['pexpect']
)
