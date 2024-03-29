import sys
from setuptools import setup

requirements = []

py3_requirements = [
    'psutil==5.6.6',
    'pytest-mock==3.6.1'
]

if sys.version_info[0] == 2:
    with open('py2requirements.txt') as f:
        py2_requirements = f.read().splitlines()
    requirements += py2_requirements
else:
    requirements += py3_requirements

setup(name='glogging',
      version='0.5.3',
      description='GI logger',
      classifiers=['Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.9'],
      url='http://github.com/pelucid/glogging',
      packages=['glogging'],
      install_requires=requirements)
