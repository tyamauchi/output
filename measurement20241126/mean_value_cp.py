import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import time

# Number of stocks
n = 90

# Indices for stocks (1 to n)
i = np.arange(1, n + 1)

# Mean returns for each stock
p = 1.15 + i * 0.05 / 150

# Standard deviations of returns
sigma = 0.05 / 450 * (2 * i * n * (n + 1))**0.5

# Constant phi for regularization term (risk aversion)
phi = 5

# Create decision variable for fractions of investment in each stock
x = cp.Variable(n)

# Covariance matrix (diagonal matrix with squared standard deviations)
Q = np.diag(sigma**2)

# Objective: maximize portfolio return minus risk (mean-variance objective)
objective = cp.Maximize(p @ x - phi * cp.quad_form(x, Q))

# Constraints: sum of investments is 1 (fully invested portfolio)
constraints = [cp.sum(x) == 1, x >= 0]

# Define the optimization problem
problem = cp.Problem(objective, constraints)

# Start measuring time
start_time = time.time()

# Solve the problem using the ECOS solver
problem.solve(solver=cp.ECOS)

# End measuring time
end_time = time.time()

# Get the optimal investment fractions and objective value
x_sol = x.value
obj_val = problem.value

# Plot the optimal investment fractions
plt.plot(range(1, n+1), x_sol, linewidth=2, color='b')
plt.xlabel('Stocks')
plt.ylabel('Fraction of investment')
plt.title('Optimal Investment Fractions')
plt.show()

# Print the objective value
print(f"Objective value: {obj_val:0.4f}")

# Print the processing time
print(f"Processing time: {end_time - start_time:.4f} seconds")
