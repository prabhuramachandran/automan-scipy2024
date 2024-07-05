---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Advanced topics

**Prabhu Ramachandran and Pawan Negi**

**SciPy 2024**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## More specification of number of cores

- Every simulation is not same
    - They have different level of computation requirement
- Options to set specific computation requirement 
    - `n_core`: Used for scheduling
    - `n_thread`: Used to set number of threads
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## How it's done

<!-- #endregion -->
```python
%load ../code/advanced/automate_num_thread.py
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Distributing simulations across computers 

- Running `n` simulations across `n` remote computers
- A simple command 
```bash
$ python automate.py -a user@hostname
```
adds the `user@hostname` to `config.json`

- If required edit `.automan/bootstrap.sh` which is copied to the remote
- Now next time if the remote is free
  - program runs depending on free `n_core` on remote
  - outputs are copied back to local

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Try running 

```bash
# this process requires a passwordless login access to ssh
# for now type your password at every prompt
# make sure your system allows remote login
$ python automate2.py -a yourusername@localhost
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Clusters with SLURM

- automan can be used within cluster
- Once it captures a compute node, automan runs all cases in that node
- A Portable Batch System (PBS) file is used to schedule jobs
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Let's see an example of a PBS file 
```bash
#!/bin/bash
#PBS -N reentry
#PBS -l select=1:ncpus=32
#PBS -j oe
#PBS -V
#PBS -o out.log
#PBS -q regular 

echo "Starting at $(date)"

cd $PBS_O_WORKDIR

#cat $PBS_NODEFILE.

micromamba activate pysph-cbc
export PYTHONPATH="$(pwd):$PYTHONPATH"
python automate.py

echo "Stopping at $(date)"
 ```


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## ML/AI example

- automan is not ideal during development of machine-learning models
- One can easily do parameter sweeps to produce insights
- An example of parameter list for a neural network
  - Network width and depth
  - activation function
  - Number of test samples
  - Number of training samples
- A helful post process routine
  - Plotting the variation of the loss with different activation function

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Adding arbitrary tasks

- An example: running latex on a manuscript
- Add a task using

```bash
from automan.api import FileCommandTask
task = FileCommandTask(
'latexmk manuscript/paper.tex -pdf -outdir=manuscript',
['manuscript/paper.pdf']
)
automator.add_task(task, name='genpdf', post_proc=True) 
```
- `genpdf`: Name of the task
- Run the task using
```bash
python automan.py genpdf
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Non-Python programs

- Program written in any other language can be automated
- `automate_c.py` automates a c++ program
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## The C++ program

- compile power.cpp using 
```bash
$ g++ power.cpp -o power.out
```
- Unlike python we require to create input file
- Create a txt file with two line
  - Output directory name
  - power input
- Run the program
```bash
$ ./power.out input.txt
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Automating the C++ code 
<!-- #endregion -->
```python
%load ../code/advanced/automate_c.py
```


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Task dependencies

- Some simulations require input which is an output of another simulation
- We can create these kind of dependencies in `automan`
- Let's create two Problems on which powers.py depend
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Let's look at the implemetation 
<!-- #endregion -->
```python
%load ../code/advanced/automate_depend.py
```

<!-- #endregion -->
