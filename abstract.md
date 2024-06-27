Title: Automate your research with automan

Track: Tutorials

## Description

In research involving any kind of computer simulation, we often have to
execute several simulations that might become a part of the final manuscript.
It is found that automating these simulations and their post-processing
introduces significant personal benefit in the form of improving research
output and productivity. Automation makes it much easier to run large
parameter sweeps and studies and allows you to focus on the important
questions to ask rather than managing hundreds or thousands of simulations
manually. This takes the drudgery of data/file management out of your hands,
systematizes your research, and makes it possible to incrementally improve and
refine your work. The added nice benefit is that your research also becomes
much easier to reproduce.

In this tutorial we introduce you to a simple package called automan
(https://automan.readthedocs.io) which facilitates automation. Automan can
automate a code written any language as long as it can be executed using a
terminal command. Additionally, a parameter sweep is possible when the program
parameters are adjustable via command line options.

We'll walk through using the automan package using some simple examples to
show how it works. We will then help you with your own research and help you
automate your own simulations to the extent possible. Our hope is at the end
of the tutorial you will be exposed to the features provided by automan and
can use it to automate your research work and boost your own productivity.

All you need to know is basic Python, some matplotlib, and no discomfort
using command-line tools (if your head spins at seeing a command prompt,
this tutorial may give you a headache). 

We expect this to be useful to anyone performing numerical simulation for
their research be it traditional numerical methods research or ML/AI
workflows.

We hope to help you automate one of your current research studies or
publication during the tutorial. So come join us, bring your work along, we
will work with you to help automate the simulations, and you can have some fun
doing it.


## Outline

- Introduction (10m)

- Getting started with a toy simulation (20m)

- Doing things better (25 m)

- Break (10m)

- Generating simulations for parameter sweeps (25m)

- Filtering and comparing simulations (25 m)

- Break (10 m)

- Distributing simulations across computers (20m)

- Advanced topics (15 m)
    - Adding arbitrary tasks
    - More complex dependencies

- Using this for your research (60 m)


## Prerequisites

- Knowledge of programming with Python. We will expect that you know what a
  class is and how you can subclass it.
- Some experience with using command line tools is necessary. You should also
  be comfortable writing a Python program that takes command line
  arguments.
- Knowledge of basic python environment management (virtualenvs or conda envs).
- Knowledge of basic numpy and matplotlib will be useful but not mandatory.

- For setup you will require a working Python installation within a
  self-contained environment and also install automan with `pip install
  automan`.


## Bios

Prabhu Ramachandran is a faculty member at the Department of Aerospace
Engineering, IIT Bombay. He has run several workshops at SciPy which have been
generally well received. See here https://www.youtube.com/watch?v=r6OD07Qq2mw
and https://www.youtube.com/watch?v=2dd4BduDkG8.  Prabhu has been using Python
for more than two decades and has been teaching Python and Python related
tools in various capacities for many years. Prabhu is also the main author of
automan which he wrote to save himself from dealing with the drudgery of
management of hundreds of simulation results for one of his papers.  Prabhu
also gave a talk on automan at SciPy 2022 titled "The (Surprising) Road to
Reproducibility: Automation!" which you can see here
(https://www.youtube.com/watch?v=zvBotV6r9AY).

Pawan Negi is a post-doctoral researcher at the Department of Applied
Mathematics, Illinois institute of Technology. He has been teaching
mathematics courses to undergraduate students since last year. He earned his
PhD at IIT Bombay, where he extensively utilized automan to execute hundreds
of test cases for his thesis. He also contributed pull requests towards the
development of automan.


## For the reviewers of this abstract

Almost the entire session will be hands on. Barring the introduction and
explanation of features, we will be asking the audience to write code as we go
along.  We will provide skeleton files for the attendees to start quickly. At
the end we have reserved a full hour to help the attendees use what we teach
for their own research work.

A somewhat complete automan tutorial is available at
https://automan.readthedocs.io/en/latest/tutorial.html and a set of
research papers that employ automan to make their work reproducible are
available at https://gitlab.com/pypr

While we will reuse content from the official tutorial, it will be done in a
way that attendees get a complete hands-on introduction.
