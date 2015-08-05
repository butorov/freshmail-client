#!/usr/bin/env python
# coding: utf-8
from distutils.core import setup


requirements = [
    'ujson',
    'requests',
]

test_requirements = [
    'pytest',
]

setup(
    name='freshmail-client',
    version='0.1',
    packages=['freshmail'],
    url='https://github.com/butorov/freshmail-client',
    author='Butorov Viacheslav',
    author_email='butorovv@gmail.com',
    description='Freshmail client for Python',
    install_requires=requirements,
    tests_require=test_requirements,
)
