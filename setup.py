#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = [
    'gitpython',
    'requests',
]

TEST_REQUIREMENTS = [
    'pytest',
]

setup(
    name='packyou',
    version='0.1.5',
    description="Downloads or clones a python project from github and allows to import it from anywhere. Very useful when the repo is not a package",
    long_description=README + '\n\n' + HISTORY,
    author="Leonardo Lazzaro",
    author_email='llazzaro@dc.uba.ar',
    url='https://github.com/llazzaro/packyou',
    packages=find_packages(),
    package_dir={'packyou':
                 'packyou'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license="MIT license",
    zip_safe=False,
    keywords='packyou',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
)
