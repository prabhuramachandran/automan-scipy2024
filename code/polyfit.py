import numpy as np
from os.path import join
import argparse


def f(x):
    return np.sin(x)


def l2_error(y, yc):
    return np.sqrt(np.sum((y - yc)**2)/len(y))


def fit(n_train:int=10, n_test:int=20, noise:float=0.1, order:int=1, 
        distrib:str='unif', output_dir:str='.'):
    assert distrib in ['normal', 'unif']
    x = np.linspace(0, 2*np.pi, n_train)
    y_exact = f(x)
    if distrib == 'normal':
        yp = noise*np.random.normal(loc=0, scale=1, size=n_train)
    elif distrib == 'unif':
        yp = noise*np.random.random(size=n_train)

    ydata = y_exact + yp

    coeffs = np.polyfit(x, ydata, order)
    p = np.poly1d(coeffs)

    y = p(x)
    train_err = l2_error(y, y_exact)

    x_test = np.linspace(0, 2*np.pi, n_test)
    y_test = p(x_test)
    test_err = l2_error(y_test, f(x_test))

    if output_dir is not None:
        fname = join(output_dir, 'results.npz')
        np.savez(fname, x=x, y_data=ydata, y_exact=y_exact, x_test=x_test, 
                 y_test=y_test, test_err=test_err, train_err=train_err)

    from matplotlib import pyplot as plt
    plt.plot(x, ydata, 'o', label='raw data')
    plt.plot(x, y_exact, label='exact')
    plt.plot(x, y, label='train')
    plt.plot(x_test, y_test, label='test')
    plt.legend()
    plt.savefig(join(output_dir, 'plot.png'))

    return train_err, test_err


def main():
    np.random.seed(123)

    p = argparse.ArgumentParser()
    p.add_argument(
        '--n-train', type=int, default=10,
        help='Number of training points'
    )
    p.add_argument(
        '--n-test', type=int, default=20,
        help='Number of test points'
    )
    p.add_argument(
        '--noise', type=float, default=0.1,
        help='Intensity of noise in data'
    )
    p.add_argument(
        '--order', type=int, default=1,
        help='Order of polynomial'
    )
    p.add_argument(
        '-d', '--output-dir', type=str, default='.',
        help='Output directory to generate file.'
    )

    p.add_argument(
        '--distrib', choices=['normal', 'unif'], default='unif',
        help='Distribution of the random noise'
    )
    opts = p.parse_args()

    train_err, test_err = fit(
        opts.n_train, opts.n_test, opts.noise, opts.order, opts.distrib,
        opts.output_dir
        )
    print(f"Training error = {train_err}, test error = {test_err}")


if __name__ == '__main__':
    main()
