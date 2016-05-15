import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__),
	'README.rst')) as readme:
		README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), 
	os.pardir)))

setup(
	name='reConstruct',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='BSD License',
	description='A Django app to conduct web-based searches of nearby waste',
	'processors for construction projects.',)
	long_description=README,
	url='',
	authors='Robert Alford, Eric Vegors, Joseph Cardenas',
	author_email=''
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 1.9',
		'Intended Audience :: Professional Contractors, Home Owners',
		'License :: OSI Approved :: BSD License', # should talk to team on this
		'Operating System :: OS Independent',
		'Programming Language :: Python',	
		'Programming Language :: Python :: 3',
		'Programming Languagae :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
],
) 
