# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kaggle-aws',
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Alexandre Maia',
    author_email='alexandre.maia@gmail.com',
    url='https://github.com/cxz/kaggle-aws',
    license=license,    
    packages=find_packages(exclude=('tests', 'docs')),
    include_packages_data=True,
    entry_points='''
        [console_scripts]
        klaws=klaws.main:main
    '''
)