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
- Using these option in `Simulation`
```python

Simulation(root=self.input_path(i),
          base_command='python print_n_thread.py',
          job_info=dict(n_core=1, n_thread=i),
)
```
```bash
$ python automate_num_thread.py
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Distributing simulations across computers 

- Running `n` simulations across `n` remote computers
- A simple command 
```python
python automate.py -a user@hostname
```
adds the `user@hostname` to `config.json`

- If required edit `.automan/bootstrap.sh` which is copied to the remote
- Now next time if the remote is free
  - program runs depending on free `n_core` on remote
  - outputs are copied back to local

```bash
$ python automate2.py -a user@localhost
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Clusters with SLURM

- `automan` can be used within cluster
- Example of a Portable Batch System (PBS) file
```
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
- Once it captures a compute node, `automan` runs all cases in that node


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## ML/AI example

- `automan` is not ideal during development of machine-learning models
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

```python
from automan.api import FileCommandTask
task = FileCommandTask(
'latexmk manuscript/paper.tex -pdf -outdir=manuscript',
['manuscript/paper.pdf']
)
automator.add_task(task, name='genpdf', post_proc=True) 
```
- `genpdf`: Name of the task
- Run the task using
```python
python automan,py genpdf
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Non-Python programs

- Program written in any other language can be automated
- `automate_c.py` automates a c++ program
- Unlike python we require to create input file
```python
def create_input(self, i):
      dir = self.simulation_path(str(i))
      power = float(i)

      os.makedirs(dir, exist_ok=True)
      fp = open(os.path.join(dir, 'input.txt'), 'w')
      fp.writelines(dir + '\n' + str(power))
      fp.close()
``` 
- Pass the input file in `base_cmd`
```python
base_cmd = './power.out $output_dir' + '/input.txt'
```
```bash
$ python automate_c.py
```


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Task dependencies

- Some simulations require input which is an output of another simulation
- We can create these kind of dependencies in `automan`
- Let's create two Problems on which powers.py depend
```python
class PowersPreCalc(Problem):
  ...

class PowersPrePreCalc(Problem):
  ...
```
- The problem `Powers` depends on `PowersPreCalc`, we code this using
```python
def get_requires(self):
  tasks = super(Powers, self).get_requires()
  tasks.extend([('a', PowersPreCalc(self.sim_dir, self.out_dir))])
  return tasks
``` 
- In `PowersPreCalc` add depdency in `PowersPrePreCalc` 
```python
def get_requires(self):
  tasks = super(PowersPreCalc, self).get_requires()
  tasks.extend([('a', PowersPrePreCalc(self.sim_dir, self.out_dir))])
  return tasks
```
```bash
$ python automate_depend.py
```

<!-- #endregion -->
