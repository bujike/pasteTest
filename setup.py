#! /usr/lib/env python
# -*- coding: utf-8 -*-

""" created by yang on 2016/7/7
"""
from setuptools import setup, find_packages
__author__ = "muyidixin2006@126.com"
setup(
    name="pasteTest",
    version='0.1',
    description="pasteTest",
    author="megoo",
    install_requires=[
        "paste",
        "webob",
        "routes"
    ],

    packages=find_packages(),
    data_files=[
        ('/etc/pasteTest', ['paste.ini'])
    ],
)
