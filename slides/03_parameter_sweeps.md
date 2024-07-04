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

**Prabhu Ramachandran and Pawan Negi**

**SciPy 2024**

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Performing Parameter Sweeps

- Common requirement
- `automan` provides tools to generate multiple parameters

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Facilitating parameter sweeps

- Use `mdict`, `dprod`

<!-- #endregion -->

```python
from automan.api import mdict, dprod, opts2path
```

```python
opts = mdict(nx=[10, 20], re=[100, 200])
opts
```

```python
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

- Use `opts2path`

<!-- #endregion -->

```python
[opts2path(x) for x in all_opts[:3] ]
```

```python
opts2path(all_opts[5])
```


<!-- #region slideshow={"slide_type": "slide"} -->
## Putting it all together

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Exercise

<!-- #endregion -->