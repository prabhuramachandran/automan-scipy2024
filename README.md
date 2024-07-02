# Automate your research with automan

This workshop will show you how you can productively manage your numerical
simulations and fully automate your research publication outputs using
[automan](https://automan.readthedocs.io).

Our research group has found using automan very helpful and also made us more
productive as it eliminates much of the drudgery of managing simulations. The
upshot is that using automan also makes it much easier for anyone to reproduce
our research. You can find over a dozen fully automated papers from here:
https://gitlab.com/pypr

See a short [SciPy 2022 presentation on
automan](https://www.youtube.com/watch?v=zvBotV6r9AY) for a quick overview of
automan.  This workshop will get you acquainted with automan and help you use
it to automate your own research manuscripts.

Join us at the workshop if you would like to:

- organize your simulations,
- manage multiple simulations with minimal fuss,
- generate all simulations and figures for your manuscript with a single command,
- distribute and execute your simulations efficiently and automatically.

We will help you with your manuscripts during the workshop, so do join us on
9th July 2024 at the [SciPy 2024](https://www.scipy2024.scipy.org/) workshops
in Tacoma, WA.

## Installation instructions

### Basic
* Create and activate the python environment with `python>=3.7.16`. This can be
  achieved by following instructions in any of the links below
    - Using conda: [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - Using python venv: [here](https://docs.python.org/3/library/venv.html)
* Do `pip install automan matplotlib numpy scipy`


### Advanced

* Download the automan package.
    - Using git clone:
		`git clone https://github.com/pypr/automan.git`
    - Use the link below to download the package and unzip the files: [here](https://github.com/pypr/automan/archive/refs/heads/master.zip)
* Change directory using `cd automan`. For windows, use `Command Prompt` or `Conda Prompt` and find the downloaded files.
* Install automan using `python install setup.py`
* We will require some packages to draw plots and to make demo calculations. Install them using `pip install matplotlib numpy scipy sympy`

## Testing the installation

* In order to test the setup do `pip install pytest`
* run `pytest --pyargs automan.tests.test_jobs automan.tests.test_utils automan.tests.test_automation` 

## Prerequisites

- Knowledge of programming with Python. We will expect that you know what a
  class is and how you can subclass it.
- Some experience with using command line tools is necessary. You should also
  be comfortable writing a Python program that takes command line
  arguments.
- Knowledge of basic python environment management (virtualenvs or conda envs).
- Knowledge of basic numpy and matplotlib will be useful but not mandatory.

