import os
import re

from setuptools import find_packages, setup

def get_version(package):
    # Thanks to Tom Christie
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def read_md(path):
    try:
        import pypandoc
        return pypandoc.convert(path, 'rst')
    except ImportError:
        return open(path).read()


version = get_version('django_thrift')


setup(
    name="django-thrift",
    version=version,
    packages=find_packages("."),
    include_package_data=True,
    description='Django App to Run a Apache Thrift RPC Server',
    long_description=read_md('README.md'),
    url='https://github.com/dstarner15/django_thrift',
    author='Daniel Starner',
    author_email="starner.daniel5@gmail.com",
    install_requires=['django', 'thriftpy', 'thrift', 'gunicorn_thrift', 'pytz'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)