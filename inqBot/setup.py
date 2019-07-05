#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='inqBot',
      version=read('VERSION'),
      description='Dungeons and Dragons 5e Character and monster generator',
      long_description=read('README.rst'),
      long_description_content_type='text/x-rst',
      keywords='D&D character sheets',
      author='Orion Collins',
      author_email='collinso@wit.edu',
      license='GPLv3',
      url='https://github.com/collinso23/discord_Project',
      download_url='https://github.com/collinso23/discord_Project',
      packages=find_packages(),
      package_data={
          'inqGen': ['forms/*pdf', 'forms/*.tex', 'forms/*.txt', '../VERSION']
      },
      install_requires=[
          'fdfgen', 'npyscreen', 'jinja2', 'pdfrw', 'BeatifulSoup', 'lxml', 'textwrap',
         'nltk', 'discord', 'numpy'
      ],
      entry_points={
          'console_scripts': [
              'makesheets = utils.make_sheets:main',
              'create-character = utils.create_character:main',
          ]
      },
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Games/Entertainment :: Role-Playing',
      ],
)
