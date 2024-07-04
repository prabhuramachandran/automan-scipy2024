from automan.api import Problem, Automator, Simulation
from matplotlib import pyplot as plt
import numpy as np
import os


class Powers(Problem):
    def setup(self):
        base_cmd = './power.out $output_dir' + '/input.txt'
        self.cases = [
            Simulation(
                root=self.simulation_path(str(i)),
                base_command=base_cmd,
            )
            for i in range(1, 5)
        ]

        for i in range(1,5):
            self.create_input(i)

    def create_input(self, i):
        dir = self.simulation_path(str(i))
        power = float(i)

        os.makedirs(dir, exist_ok=True)
        fp = open(os.path.join(dir, 'input.txt'), 'w')
        fp.writelines(dir + '\n' + str(power))
        fp.close()

    def run(self):
        self.make_output_dir()


if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Powers]
    )
    automator.run()
