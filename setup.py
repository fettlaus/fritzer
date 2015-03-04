#!/usr/bin/env python

from distutils.core import setup

setup(name='Fritzer',
      version='0.0.1',
      description='Unblock-US Updater by FritzBox IP',
      author='Fettlaus',
      author_email='Fettlaus@gmail.com',
      url='https://projects.fettlaus.de/python/fritzer',
      packages=['fritzer'],
      install_requires=[
          'fritzconnection',
      ],
      scripts=['fritzer/fritzer'],
     )
