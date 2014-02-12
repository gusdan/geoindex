#!/usr/bin/env python

from setuptools import setup


README = open('README.rst').read()
VERSION = '0.1'

setup(
    name='geoindex',
    version=VERSION,
    description=('Simple library for perform quick nearby search '
                 'for geo spatial data.'),
    long_description=README,
    author='Danil Gusev, Igor Davydenko',
    author_email='dgusev@getgoing.com',
    url='http://github.com/getgoing/geoindex',
    packages=[
        'geoindex',
    ],
    install_requires=[
        'eventlet>=0.13.0',
        'ujson>=1.33'
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
