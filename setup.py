#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import re


# Utilities
with open('README.md') as readme_file:
    readme = readme_file.read()


def find_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('popularipy/__init__.py').read())
    return result.group(1)



# Setup
setup(
    author="Dominique Makowski",
    author_email='dom.makowski@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Access popularity metrics for your python package.",
    install_requires=['pandas', 'pypistats', 'neurokit2', 'json', ],
    license="GNU license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='popularipy',
    name='popularipy',
    packages=find_packages(),
    # package_data = {"popularipy.layouts":["*.txt"]},
    setup_requires=setup_requirements,
    test_suite='pytest',
    tests_require=test_requirements,
    url='https://github.com/DominiqueMakowski/popularipy',
    version=find_version(),
    zip_safe=False,
)
