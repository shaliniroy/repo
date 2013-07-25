#!/usr/bin/env python
"""Dummy Project"""
from setuptools import find_packages, setup

dependencies = [
        'setuptools',
        'requests',
        'cmd2',
    ]

setup(name = 'shellproject',
    version = '1',
    description = "shell",
    long_description = "shell",
    platforms = ["Linux"],
    author = "Shalini Roy",
    author_email = "shaliniroy012@gmail.com",
    url = "http://dgplug.org/summertraining/2013/",
    license = "MIT",
    packages = find_packages(),
    install_requires = dependencies,
    include_package_data=True,
    scripts=['shellproject'],
    data_files=[('/usr/bin',['shell']),
    ('/usr/share/shell', ['README'])
    ]

    )
