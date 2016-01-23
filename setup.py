# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ghp',
    version='0.1.0',

    description='GitHub command line tools made with Python',
    long_description=long_description,

    url='https://github.com/tomochikahara/ghp',

    author='Tomochika Hara',
    author_email='tomochika1985@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='github issue pull-request cli',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'PyGithub==1.26.0'
    ],

    entry_points={
        'console_scripts': [
            'ghp=ghp:main',
        ],
    },
)
