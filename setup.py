#!/usr/bin/env python

from setuptools import setup


setup(
    name='geoindex',
    version='0.0.1',
    description=('Simple library for perform quick nearby search '
                 'for geo spatial data.'),
    long_description=open('README.rst').read(),
    author='Danil Gusev',
    author_email='gusev.danil@gmail.com',
    url='http://github.com/gusdan/geoindex',
    packages=[
        'geoindex',
    ],
    install_requires=[
        'python-geohash>=0.8.4',
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='geo index spatial geohash indexer grid',
    license='BSD License',
)
