#!/usr/bin/env python3

from setuptools import setup, find_packages

import os


def read_requirements():
    """Parse requirements from requirements.txt."""
    requirements_path = os.path.join('.', 'requirements.txt')
    with open(requirements_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name                = 'mediacon-py',
    version             = '1.0001',
    description         = 'Find usernames in social networks.',
    author              = 'Mukesh',
    url                 = 'https://github.com/Mukesh-creator/mediacon',
    packages            = find_packages(),
    scripts             = ['mediacon-py'],
    install_requires    = read_requirements(),
    classifiers = [
        'Programming Language :: Python3',
        'Environment :: Console',
    ],
)

