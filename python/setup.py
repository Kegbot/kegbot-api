#!/usr/bin/env python

"""Kegbot API client library.

For more information and documentation, see http://kegbot.org/docs
"""

from setuptools import setup, find_packages

VERSION = '0.1.4'
DOCLINES = __doc__.split('\n')
SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])

def setup_package():

  setup(
      name = 'kegbot-api',
      version = VERSION,
      description = SHORT_DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      author = 'mike wakerly',
      author_email = 'opensource@hoho.com',
      url = 'http://kegbot.org/',
      packages = find_packages(exclude=['testdata']),
      namespace_packages = ['kegbot'],
      install_requires = [
        'kegbot-pyutils >= 0.1.4',
        'python-gflags >= 1.8',
        'protobuf >= 2.4.1',
        'requests',
      ],
      include_package_data = True,
      dependency_links = [
          'https://github.com/rem/python-protobuf/tarball/master#egg=protobuf-2.4.1',
      ],
  )

if __name__ == '__main__':
  setup_package()
