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
# Automate your research with automan

**Prabhu Ramachandran and Pawan Negi**

**SciPy 2024**

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->

<center>
<h1> Welcome! </h1>
</center>

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->

## Backdrop

>   An article about computational science in a scientific publication is
>   not the scholarship itself, it is merely advertising of the
>   scholarship. The actual scholarship is the complete software
>   development environment and the complete set of instructions which
>   generated the figures.

<p style="text-align: right">
-- Buckheit, J. and Donoho, D. L. (paraphrasing Jon F. Claerbout)
<p>

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Background

- Numerical methods papers require a lot of computation
- We make mistakes in papers
   - Typos
   - Missing or wrong parameters
- Code availability is a problem
- Management of simulation data
- Dealing with reviewer comments months afterward

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## A modest reproducibility goal

<br/>
<br/>

- Can you, reproduce your paper results, after a year?
- Can you reproduce results of a colleague's paper who works in the same area?

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Goals

- Use [automan](https://github.com/pypr/automan) for your research output/publication
- Automate your manuscript
    - All simulations
    - All figures

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Pre-requisites

- Basic knowledge of Python
- Using classes in Python
- Comfort with using the command line prompt

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Automan helps you

- organize your simulations
- orchestrate running simulations and do post-processing
- reuse code for post processing
- generate all simulations and figures with one command
- optionally distribute simulations among other computers


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Best usage recommendations

Your programs should:

1. be configurable using command line arguments

2. generate output files in directory specified on command line

3. save post-processed data into a datafile and not just create plots


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Why automan and not xyz?

- Other tools:
    - [mlflow](https://mlflow.org)
    - [guild.ai](https://guild.ai)
    - [sacred](https://sacred.readthedocs.io)
    - [neptune.ai](https://neptune.ai)

- Automan is designed for the numerical methods workflow

- Automan is non-intrusive

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## How does this help us?

- Have a dozen automated papers
   - https://gitlab.com/pypr
   - https://github.com/nn4pde

- Everyone in the lab automates (by default!)

- Much easier to incrementally do research

- Less stress

- Easy to make changes (even months after submission!)

- Exploration is driven by `automan`

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Bottom line

- It takes some effort to use automan
- But ... the results are well worth it

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Learn the general approach to automation

<br/>

- Want to learn the general approach

- automan is one particular option
- Can use any other tool also

<!-- #endregion -->