import sys
from setuptools import setup

requirements = []

py3_requirements = [
    'psutil==5.6.6'
]

if sys.version_info[0] == 2:
    with open('py2requirements.txt') as f:
        py2_requirements = f.read().splitlines()
    requirements += py2_requirements
else:
    requirements += py3_requirements

setup(name='glogging',
      version='0.5',
      description='GI logger',
      url='http://github.com/pelucid/glogging',
      packages=['glogging'],
      install_requires=requirements)
