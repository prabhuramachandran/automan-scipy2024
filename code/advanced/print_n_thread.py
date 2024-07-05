import argparse
import os

import numpy as np


def print_n_cores():
    """Print the environment variable OMP_NUM_THREADS 
    """
    os.system('echo number of threads are set to $OMP_NUM_THREADS')


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        '--output-dir', type=str, default='.',
        help='Output directory to generate file.'
    )
    opts = p.parse_args()
    print_n_cores()



if __name__ == '__main__':
    main()
