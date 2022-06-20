#!/usr/bin/env python

try:
  import os
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

setup(
  name = 'pyzipcode-cli',
  version = '0.1.4',
  author = 'Dalwinder singh',
  author_email = 'prodicus@gmail.com',
  description = "a thin wrapper around getziptastic's API v2",
  url = 'https://github.com/dalwindr/inferzipcode.git',
  license = 'MIT',
  install_requires = [
    "pandas==1.4.0"
  ],
  ### adding package data to it 
  packages=find_packages(exclude=['contrib', 'docs']),
  # package_data={
  #     'assets': ['*.json'],
  # },

  download_url = 'https://github.com/dalwindr/inferzipcode.git/tarball/0.1.0',
  classifiers = [
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: not OSI Approved :: MIT License',

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
  ],
  keywords = ['api', 'geo-location', 'zipcode','devtools', 'Development', 'ziptastic', 'latitude', 'longitude'], 
  entry_points = {
        'console_scripts': [
            'pyworldpostal = pyworldpostal.core:main'
      ],
    }
)
