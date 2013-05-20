# -*- coding: utf-8 -*-
import os
from django_wiki_formulas import VERSION
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

packages = find_packages()

setup(
    name = "django-wiki-formulas",
    version = VERSION,
    author = "Thomas Lottermann",
    author_email = "TomLottermann@googlemail.com",
    url = "https://github.com/TomLottermann/django-wiki-formulas",
    description = ("A simple formula plugin for wiki (django-wiki)."),
    license = "GPLv3",
    keywords = "django wiki formula",
    packages = find_packages(),
    long_description = read('README.md'),
    zip_safe = False,
    install_requires = read('requirements.txt').split("\n"),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    include_package_data = True,
)
