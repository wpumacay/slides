# Tutorial 0 - playing around with some environments

## Setting up

There are quite a few environment we will be using. Most dependencies
are installed via pip with the requirements.txt file provided, but some
require installation through conda packages. Below there are some steps
to follow in order to start playing around with these environments in
the provided notebook.

### Our base environment

We'll hope for the best and assume that all packages won't have conflicting
dependencies :O. So, for the sake of time let's just create a single conda
environment and place everything in there before testing the notebook.

```bash
# create the before mentioned conda environment
conda create -n rl_tutorial0_env python=3.6.1

# and just activate it and install everything in there
source activate rl_tutorial0_env

# install all dependencies from the requirements.txt file
pip install -e .
```

### OpenAI-Gym

Gym is pretty easy to install. There's already a pip package that we already
installed along the previous requirements, so we are good to go.

### Osim-rl

You can find the repo [here](https://github.com/stanfordnmbl/osim-rl). It consists
of an rl environment that runs on top of the OpenSim simulator, which seems to be
quite good for biomechanics-physics simulations.

First, install the required conda packages:

```bash
# install some required conda-packages
conda install -c kidzik opensim
conda install -c conda-forge lapack git

# install the osim-rl
pip install osim-rl
```

### Mine-rl

This one is a set of environment extracted from Project MALMO, and it's used for
a competition at NeurIPS-2019. The repo can be found [here](https://github.com/minerllabs/minerl).
To start using the package just run the following:

```bash
# install openjdk
sudo apt-get install openjdk-8
# make sure you're on your conda environment
source activate rl_tutorial0_env
# instal the pip package for mine-rl
pip install minerl
```
