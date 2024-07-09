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
# Parameter sweeps

<br/>
<br/>

**Prabhu Ramachandran and Pawan Negi**

<br/>

**SciPy 2024**

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Performing Parameter Sweeps

- Common requirement
- `automan` provides tools to generate multiple parameters

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Facilitating parameter sweeps

- `mdict`: product of passed kwargs into a list of dicts
- `dprod`: product of given dictionaries
- Learn with examples below

<!-- #endregion -->

```python
from automan.api import mdict, dprod
```

```python
opts = mdict(nx=[10, 20], re=[100, 200])
opts
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Exercises

- Given three parameters
  - `n` which we want values in [5, 10, 15]
  - `order` which is an integer in [1, 2, 3]
  - `func` which is either `'sin`' or `'gaussian'`
- Generate the product of each of these as a list of dictionaries using mdict

<!-- #endregion -->

```python
# Your code here.
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Solution
<!-- #endregion -->

```python
mdict(n=[5, 10, 15], order=[1, 2, 3], func=['sin', 'gaussian'])
```

<!-- #region slideshow={"slide_type": "slide"} -->
## More complex options

- See the following example
- Have the `nx, re` parameters as before
- Also have two optimizers with their learning rates
- Want the appropriate product of these
<!-- #endregion -->

```python
opts = mdict(nx=[10, 20], re=[100, 200])
opts2 = (mdict(optimizer=['Adam'], lr=[1e-2, 1e-3]) +
         mdict(optimizer=['LBFGS'], lr=[1.0, 0.1]))
opts2
```

```python
all_opts = dprod(opts, opts2)
all_opts
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Generating unique and sensible directory names

- `mdict, dprod`: create parameter varations
- However, we need unique directory names for each case!

- Use `opts2path`

<!-- #endregion -->

```python
from automan.api import opts2path
```

```python
[opts2path(x) for x in all_opts[:3] ]
```

```python
opts2path(all_opts[5])
```

```python
# More options
opts2path?
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Summary

- Use `mdict, dprod` to generate options
- Use `opts2path` to generate suitable directory names
- Using these you can create `Simulation` instances as required

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
## Exercise

- Look at `code/polyfit.py`
- Start with the `code/automate_polyfit.py` 
- Modify it to perform the fit for different order polynomials from 1 to 8 and
  compare the training and test error

<!-- #endregion -->