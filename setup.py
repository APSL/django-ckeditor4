import os
from setuptools import setup, find_packages

install_requires = []
try:
    import json
except ImportError, e:
    install_requires.append('simplejson')

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

description = 'A small Django application that makes it easy to use CKEditor4 for form textareas.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description


setup(
    name='django-ckeditor4',
    version='0.9.3',
    install_requires=install_requires,
    description=description,
    long_description=long_description,
    author='Miketsukami',
    author_email='a.o.suhanov@gmail.com',
    url='http://bitbucket.org/Miketsukami/django-ckeditor4/',
    packages=['ckeditor'],
)
