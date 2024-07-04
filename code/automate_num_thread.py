from automan.api import Problem, Automator, Simulation
from matplotlib import pyplot as plt
import numpy as np


class NThreadProb(Problem):
    def setup(self):
        base_cmd = 'python print_n_thread.py --output-dir $output_dir'
        self.cases = [
            Simulation(
                root=self.simulation_path(str(i)),
                base_command=base_cmd,
                job_info=dict(n_core=1, n_thread=i),
            )
            for i in range(1, 5)
        ]

    def run(self):
        self.make_output_dir()

if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[NThreadProb]
    )
    automator.run()
