"""Kegboard API client library

This package contains the Python API client for Kegbot.  For more
information, see https://kegbot.org/docs
"""

from setuptools import setup, find_packages

VERSION = '1.3.2'
DOCLINES = __doc__.split('\n')
SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])

setup(
  name='kegbot-api',
  version=VERSION,
  description=SHORT_DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  long_description_content_type='text/markdown',
  author='The Kegbot Project Contributors',
  author_email='info@kegbot.org',
  license='MIT',
  url='https://kegbot.org/',
  packages=find_packages(exclude=['testdata']),
  namespace_packages=['kegbot'],
  install_requires=[
    'python-gflags >= 1.8',
    'protobuf',
    'requests',
  ],
  include_package_data=True,
)
