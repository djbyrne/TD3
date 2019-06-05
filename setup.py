#!/usr/bin/env python

from setuptools import setup, Command, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='rl_dev',
      version='1.0',
      description='Base dev environment for reinforcement learning projects',
      license='Apache License 2.0',
      author='Donal Byrne',
      author_email='donaljbyrne@me.com',
      url='',
      packages=find_packages(),
      install_requires = required,
      long_description= ("Base dev environment for reinforcement learning projects")
     )