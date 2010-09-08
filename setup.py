#!/usr/bin/env python

from setuptools import setup, find_packages

PACKAGE = 'TracGodAuth'
VERSION = '0.1'

setup(
    name=PACKAGE, version=VERSION,
    description='Trac plugin for SSO authn/authz',
    author="Cal Henderson", author_email="cal@iamcal.com",
    license='Private', url='http://code.iamcal.com',
    packages=find_packages(exclude=['ez_setup', '*.tests*']),
    package_data={
        'godauth': []
    },
    entry_points = {
        'trac.plugins': [
            'godauth.auth = godauth.auth',
            'godauth.perm = godauth.perm',
        ]
    }
)

