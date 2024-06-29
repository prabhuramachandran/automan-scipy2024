# Automate your research with automan


This currently holds the proposal being submitted to SciPy 2024. 

The repository will eventually hold the slides and examples for the tutorial.


# Installation instructions

## Basic
* Create and activate the python environment with `python>=3.7.16`. This can be
  achieved by following instructions in any of the links below
    - Using conda: [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - Using python venv: [here](https://docs.python.org/3/library/venv.html)
* Do `pip install automan matplotlib numpy scipy`


## Advanced

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