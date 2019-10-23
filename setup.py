#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
#

from setuptools import setup, find_packages

setup(
    name='hejtado-quido',
    version='0.2.2',
    description='Thermometer Quido RESTful API based on Flask-RESTPlus',
    url='https://github.com/hejtado/quido',
    author='Lumir Jasiok',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',
    include_package_data=True,
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    hejtado-quido = hejtado.quido.app:main
    """,
    install_requires=['flask-restplus==0.13.0'],
)
