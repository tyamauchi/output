from rsome import ro
from rsome import grb_solver as grb
import rsome as rso
import numpy as np

n = 150                                       # number of stocks
i = np.arange(1, n+1)                       # indices of stocks
p = 1.15 + i*0.05/150                       # mean returns
sigma = 0.05/450 * (2*i*n*(n+1))**0.5       # standard deviations of returns
phi = 5                                     # constant phi

model = ro.Model('mv-portfolio')            # create an RSOME model

x = model.dvar(n)                           # fractions of investment

Q = np.diag(sigma**2)                       # covariance matrix
model.max(p@x - phi*rso.quad(x, Q))         # mean-variance objective
model.st(x.sum() == 1)                      # summation of x is one
model.st(x >= 0)                            # x is non-negative

model.solve(grb)

import matplotlib.pyplot as plt

obj_val = model.get()               # the optimal objective value
x_sol = x.get()                     # the optimal investment decision

plt.plot(range(1, n+1), x_sol,
         linewidth=2, color='b')
plt.xlabel('Stocks')
plt.ylabel('Fraction of investment')
plt.show()
print('Objective value: {0:0.4f}'.format(obj_val))