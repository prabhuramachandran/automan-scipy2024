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
# Getting started with automan

**Prabhu Ramachandran and Pawan Negi**

**SciPy 2024**

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Installation

- Install via `pip install automan`
- We use numpy and matplotlib for our examples

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## A toy example

- Trivial example that computes the powers of the integers
- Supports command line arguments

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Best usage recommendations

Your programs should:

1. be configurable using command line arguments

2. generate their output files into a directory specified on the command line

3. save post-processed data into a datafile and not just create plots

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## `code/powers.py`
<!-- #endregion -->

```python
%load ../code/powers.py
```


<!-- #region slideshow={"slide_type": "slide"} -->
## Explore the code

- Run the example
- Look at the output


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Exercise

- Generate the cube of integers from 0 to 10
- Plot the results in the generated `results.npz`

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Solution

<!-- #endregion -->

```python
import numpy as np
data = np.load('results.npz')
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Running the simulations

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Generating output 

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Summary of workflow

<!-- #endregion -->