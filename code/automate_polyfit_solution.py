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
        opts = mdict(order=range(1, 9))
        self.cases = [
            Simulation(
                root=self.simulation_path(opts2path(opt)),
                base_command=base_cmd,
                **opt
            )
            for opt in opts
        ]

    def run(self):
        self.make_output_dir()
        # For a given n_train, change the order of polynomial and plot the
        # variation of the training and test errors.
        plt.figure()
        order = []
        test_error = []
        train_error = []
        for case in self.cases:
            data = np.load(case.input_path('results.npz'))
            order.append(case.params['order'])
            test_error.append(data['test_err'])
            train_error.append(data['train_err'])
        plt.plot(
            order, train_error, 'o',
            label='Training error'
        )
        plt.plot(
            order, test_error, '^',
            label='Testing error'
        )
        plt.grid()
        plt.xlabel('order')
        plt.ylabel('error')
        plt.legend()
        plt.savefig(self.output_path('errors.pdf'))
        plt.close()


if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Polyfit]
    )
    automator.run()
