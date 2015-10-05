#!/usr/bin/env python
# coding: utf-8
import sys
import platform

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
    'requests',
]

test_requirements = [
    'pytest==2.8.0',
    'httmock',
]

if sys.version_info[:2] == (3, 2):
    test_requirements.append('coverage==3.7.1')

JYTHON = platform.system() == 'Java'


if not hasattr(sys, 'pypy_translation_info') and not JYTHON:
    requirements.append('ujson')
if not JYTHON:
    test_requirements.append('pytest-cov')


setup(
    name='freshmail-client',
    version='0.1',
    packages=['freshmail'],
    url='https://github.com/butorov/freshmail-client',
    author='Butorov Viacheslav',
    author_email='butorovv@gmail.com',
    description='Freshmail client for Python',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    cmdclass={'test': PyTest},
)
