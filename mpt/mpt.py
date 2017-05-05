import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Varios
np.random.seed(123)
solvers.options['show_progress'] = False

# Simulating data
n_assets = 4
n_obs = 1000
return_vec = np.random.randn(n_assets, n_obs)

# Generate random weights
def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)

# Compute mean and std of portfolios return
def random_portfolio(returns):
    '''
    Returns the mean and standard deviation of returns for a random portfolio
    '''
    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))

    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)

    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return random_portfolio(returns)

    return mu, sigma


# means, stds = random_portfolio(return_vec)

# Performance of random porfolios
n_portfolios = 500
means, stds = np.column_stack([
    random_portfolio(return_vec)
    for _ in range(n_portfolios)
    ])

# print(rand_weights(n_assets))
# print(means)
# print(stds)


# Plot
plt.figure(1)
plt.plot(stds, means, 'o', markersize=5)
plt.xlabel('std of returns')
plt.ylabel('mean of returns')
plt.title('Randomly Generated Portfolios')
plt.savefig(dir_path + '/mpt.png')
