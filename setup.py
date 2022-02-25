__version__ = '0.0.1'

from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in


setup(
    name='sunkern',
    version=__version__,
    packages=find_packages(),
    description='A Discord Bot for creating Github issues.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://sunkern.pmdcollab.org',
    install_requires=[
        'gidgethub>=4.2.0',
        'discord.py>=1.5.1',
        'aiohttp>=3.7.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
