#!/usr/bin/env python

version = __import__('XdaPy').get_version()

from setuptools import setup, find_packages
setup(name='XdaPy',
      version=version,
      author='Anthony King',
      author_email='anthonydking@slimroms.net',
      description='XDA Library in Python',
      packages=find_packages(),
      )