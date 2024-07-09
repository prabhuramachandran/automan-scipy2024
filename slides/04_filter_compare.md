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
# Plotting utilities: comparing simulations

<br/>
<br/>

**Prabhu Ramachandran and Pawan Negi**

<br/>

**SciPy 2024**


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Automated plotting

- Tools for automatic plotting
- Many simulation cases
  - Need to filter a select few for a plot
  - Reduce repetitive coding for plots

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## An example
<!-- #endregion -->
```python
from automan.api import Simulation, filter_by_name, filter_cases, mdict, opts2path
opts = mdict(order=[1, 2, 3, 4], n_train=[10, 20, 30])
cases = [
  Simulation(
    root=opts2path(opt),
    base_command='python polyfit.py -d $output_dir',
    **opt
  )
  for opt in opts
]
```

```python
len(cases)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Filtering simulations

- Filter by case name: `filter_by_name`

- Filter by parameters: `filter_cases`

- Extracts only the cases where `n_train=10`:

<!-- #endregion -->


```python
filter_by_name(cases, ['n_train_10_order_1', 'n_train_10_order_2'])
```

```python
filter_cases(cases, n_train=10)
```

```python
filter_cases(cases, n_train=10, order=3)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Filtering function

- Can filter cases based on a function
- Function takes a simulation instance and returns True/False
- Example below filters all odd cases
<!-- #endregion -->


```python
filter_cases(cases, lambda x: x.params['order'] % 2)
```

```python
[x.name for x in filter_cases(cases, lambda x: x.params['order'] % 2)]
```


<!-- #region slideshow={"slide_type": "slide"} -->
## Automatic plots

- Same plot for different cases
- Can compare runs: `compare_runs`
- Example:

<!-- #endregion -->

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from automan.api import compare_runs
```

```python
def exact(case, **kw):
  x = np.linspace(0, 2*np.pi, 20)
  plt.plot(x, np.cos(x), label='Exact', **kw)

def plotter(case, **kw):
  # A plot for illustration.
  x = np.linspace(0, 2*np.pi, 100)
  w = case.params['order']
  y = np.sin(w*x)
  plt.plot(x, y, **kw)
```

```python
case10 = filter_cases(cases, n_train=10)
compare_runs(cases, plotter, labels=['order'], exact=exact)
plt.legend();
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Changing the linestyle

- The line style can be customized
- `compare_runs(sims, method, labels, exact, styles)`
- Pass the last kwarg `styles`
- The default implementation is

<!-- #endregion -->

```python
import itertools as IT

def styles(sims):
    ls = [dict(color=x[0], linestyle=x[1]) for x in
          IT.product("kbgr", ["-", "--", "-.", ":"])]
    return IT.cycle(ls)
```
<!-- #region slideshow={"slide_type": "slide"} -->
## Other style examples

<!-- #endregion -->


```python
# More colorful styles
def styles(sims):
    ls = [dict(linestyle=x[0], color=x[1]) for x in
          IT.product(["-", "--", "-.", ":"], 'kbgrycm')]
    return IT.cycle(ls)
```

```python
# Setting markerstyles
def mystyles(sims):
    ls = [dict(color=x[1], linestyle='-',
               marker=x[0], markevery=5) for x in
          IT.product([None, '^', 'o'], 'kbgrcmy')]
    return IT.cycle(ls)

```

<!-- #region slideshow={"slide_type": "slide"} -->
## Exercise

- Update the `automate_polyfit.py` to make plots
- Use the `filter*` and `compare_runs` functions
<!-- #endregion -->
