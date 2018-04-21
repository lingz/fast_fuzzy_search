#!/usr/bin/env python3

from distutils.core import setup
setup(
  name = 'fast_fuzzy_search',
  packages = ['fast_fuzzy_search'], # this must be the same as the name above
  version = '0.1.4',
  description = 'Fast fuzzy search based on phonetic indexing',
  author = 'Ling Zhang',
  author_email = 'lz@ling.nz',
  url = 'https://github.com/lingz/fast_fuzzy_search', # use the URL to the github repo
  install_requires = [
    'pyphone'
  ],
  keywords = ['search', 'indexing', 'phonetic'],
)

