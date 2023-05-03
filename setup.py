# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Settings Manager',
    version='0.0.0',
    description='Settings Manager tool that can be used to store efficiently settings at different scopes, ...',
    long_description=readme,
    author='Valentin Figué',
    author_email='valentin.figue@polytechnique.edu',
    url='https://github.com/ValentinFigue/SettingsManager',
    license=license,
    install_requires=requirements,
    packages=find_packages(exclude=('tests', 'docs'))
)