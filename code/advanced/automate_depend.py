from automan.api import Problem, Automator, Simulation
from matplotlib import pyplot as plt
import numpy as np


class Powers(Problem):
    def get_requires(self):
        tasks = super(Powers, self).get_requires()
        tasks.extend([('a', PowersPreCalc(self.sim_dir, self.out_dir))])
        return tasks
        

    def setup(self):
        base_cmd = 'python powers.py --output-dir $output_dir'
        self.cases = [
            Simulation(
                root=self.simulation_path(str(i)),
                base_command=base_cmd,
                power=float(i)
            )
            for i in range(1, 2)
        ]

    def run(self):
        self.make_output_dir()
        # Some post processing


class PowersPreCalc(Problem):
    def get_requires(self):
        tasks = super(PowersPreCalc, self).get_requires()
        tasks.extend([('a', PowersPrePreCalc(self.sim_dir, self.out_dir))])
        return tasks

    def setup(self):
        base_cmd = 'python -c "print(2)"'
        self.cases = [
            Simulation(
                root=self.simulation_path(str(i)),
                base_command=base_cmd,
            )
            for i in range(1, 2)
        ]

    def run(self):
        self.make_output_dir()


class PowersPrePreCalc(Problem):
    def setup(self):
        base_cmd = 'python -c "print(1)"'
        self.cases = [
            Simulation(
                root=self.simulation_path(str(i)),
                base_command=base_cmd,
            )
            for i in range(1, 2)
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
