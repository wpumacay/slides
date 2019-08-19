
from setuptools import find_packages
from setuptools import setup 

with open( 'requirements.txt' ) as fhandle :
    _requirements = fhandle.read().splitlines()

packages = find_packages()

setup(
    name                    = 'rl-tutorial-1',
    version                 = '0.0.1',
    description             = 'tutorial 1, which explains iterative policy evaluation|iteration and value iteration',
    keywords                = 'rl ai dl',
    packages                = packages,
    install_requires        = _requirements
)
