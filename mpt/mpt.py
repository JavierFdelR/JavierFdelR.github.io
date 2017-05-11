import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd
import os


# ------------ FUNCTIONS DEFINITIONS ------------
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

# Get optimal portfolio
def optimal_portfolio(returns):
    n = len(returns)
    returns = np.asmatrix(returns)

    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x']
                  for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns, risks





# ------------ START PLAYING ------------

# Inizializing
np.random.seed(123)
solvers.options['show_progress'] = False
dir_path = os.path.dirname(os.path.realpath(__file__))

# Simulating data
n_assets = 4
n_obs = 1000
return_vec = np.random.randn(n_assets, n_obs)

# Performance of random porfolios
n_portfolios = 500
means, stds = np.column_stack([
    random_portfolio(return_vec)
    for _ in range(n_portfolios)
    ])

# Optimal Portfolio
weights, returns, risks = optimal_portfolio(return_vec)

# Visualize Performance

weights
return_vec

N = return_vec.shape[1]
level = np.ones(N)
level[0] = 100
port_return = np.dot(return_vec.T, weights)

for i in range(1,N):
    level[i]= level[i-1] + port_return[i]


# ------------ START PLOTING ------------

# Plot 1: Histogram
a = return_vec[0,:]
plt.figure(1)
plt.hist(a, bins=np.linspace(min(a),max(a),100))
plt.xlabel('returns')
plt.ylabel('frequency')
plt.title('Simulated Returns for Stock 1')
plt.savefig(dir_path + '/mpt1.png')

# Plot 2: Portfolios
plt.figure(2)
plt.plot(stds, means, 'o', markersize=5)
plt.xlabel('std of returns')
plt.ylabel('mean of returns')
plt.title('Randomly Generated Portfolios')
plt.savefig(dir_path + '/mpt2.png')

# Plot 3: Efficient Frontier
plt.figure(3)
plt.plot(risks, returns, 'y-o')
plt.xlabel('std of returns')
plt.ylabel('mean of returns')
plt.title('Upper Efficient Frontier')
plt.savefig(dir_path + '/mpt3.png')

# Plot 4: Performance
plt.figure(4)
plt.plot(level, '-')
plt.xlabel('period')
plt.ylabel('level')
plt.title('Performance')
plt.savefig(dir_path + '/mpt4.png')
