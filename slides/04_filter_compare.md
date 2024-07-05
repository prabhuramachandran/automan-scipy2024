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

**Prabhu Ramachandran and Pawan Negi**

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

```python
compare_runs(cases, plot_function, labels=['nx'], exact=exact_plot_func)
```
- `plot_func(case, **kw)`: `kw` are plotting related kwargs

<!-- #endregion -->



