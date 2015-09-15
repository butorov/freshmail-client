#!/usr/bin/env python
# coding: utf-8
import sys

from distutils.core import setup
from setuptools.command.test import test


class PyTest(test):
    user_options = [('pytest-args=', 'a', 'Arguments to pass into py.test')]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requirements = [
    'ujson',
    'requests',
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'httmock',
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
    cmdclass={'test': PyTest},
)
