
from setuptools import find_packages
from setuptools import setup 

with open( 'requirements.txt' ) as fhandle :
    _requirements = fhandle.read().splitlines()

packages = find_packages()

setup(
    name                    = 'rl-tutorial-0',
    version                 = '0.0.1',
    description             = 'tutorial 0, which explains how to use gym and other benchmarks',
    keywords                = 'rl ai dl',
    packages                = packages,
    install_requires        = _requirements
)