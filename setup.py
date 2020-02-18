from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='isDataType',
	version='0.0.1',
	description="isDataType is a special library to check the variable data types",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/kirankotari/isDataType',
	author = 'Kiran Kumar Kotari',
	author_email='kirankotari@live.com',
	classifiers = [ 
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License', 
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		],
	keywords = 'isDataType isListInt isListFloat isListString isInt isFloat isString',
	packages = find_packages(exclude=['tests']),
)
