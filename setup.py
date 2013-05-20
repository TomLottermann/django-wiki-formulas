# -*- coding: utf-8 -*-
from django_wiki_formulas import VERSION
from setuptools import setup, find_packages

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
    include_package_data = True,
    long_description = open('README.md').read(),
    zip_safe = False,
    requires = ['wiki'],
)
