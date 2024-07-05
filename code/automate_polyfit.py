from automan.api import (
    Problem, Automator, Simulation, mdict, dprod, opts2path
)
from matplotlib import pyplot as plt
import numpy as np


class Polyfit(Problem):
    def setup(self):
        base_cmd = 'python polyfit.py -d $output_dir'
        # Generate appropriate parameter variations with mdict, dprod
        # Use opts2path to create the directories
        self.cases = [
        ]

    def run(self):
        self.make_output_dir()
        # For a given n_train, change the order of polynomial and plot the
        # variation of the training and test errors.

if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Polyfit]
    )
    automator.run()
