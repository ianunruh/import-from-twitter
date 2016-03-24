#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='import-from-twitter',
    version='0.0.1',
    description='Import Python modules from tweets',
    author='Ian Unruh',
    author_email='ianunruh@gmail.com',
    url='https://github.com/ianunruh/import-from-twitter',
    keywords=['twitter', 'import'],
    classifiers=['License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'tweepy',
    ],
)
