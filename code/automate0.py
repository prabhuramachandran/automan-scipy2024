from automan.api import Problem, Automator, Simulation
from matplotlib import pyplot as plt
import numpy as np


class Powers(Problem):
    def setup(self):
        base_cmd = 'python powers.py --output-dir $output_dir'
        self.cases = [
            Simulation(
                root=self.simulation_path('1'),
                base_command=base_cmd,
                power=1
            )
        ]

    def run(self):
        self.make_output_dir()


if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Powers]
    )
    automator.run()
