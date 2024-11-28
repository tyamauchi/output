from rsome import ro
#from rsome import grb_solver as grb
from rsome import eco_solver as ecos
import rsome as rso
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time      # 20241128

start_time = 0
end_time = 0

#N = 50
N = 55
b = 2000

c = 2*rd.randint(low=5, high=10, size=N)    # profit coefficients
w = 2*rd.randint(low=10, high=41, size=N)   # nominal weights
delta = 0.2*w                               # maximum deviations

def robust(r):
    """
    The function robust implements the robust optimiztion model,
    given the budget of uncertainty r
    """

    model = ro.Model('robust')
    x = model.dvar(N, vtype='B')    
    z = model.rvar(N)              

    z_set = (abs(z) <= 1, rso.norm(z, 1) <= r)
    model.max(c @ x)
    model.st(((w + z*delta) @ x <= b).forall(z_set))

    #model.solve(grb, display=False) # disable solution message
    model.solve(ecos, display=False) # disable solution message

    return model.get(), x.get()     # the optimal objective and solution

def robustness(tau):
    """
    The function robustness implements the robustness optimization
    model, given the profit target tau.
    """

    model = ro.Model('robustness')

    x = model.dvar(N, vtype='B')    
    k = model.dvar()              
    z = model.rvar(N)           
    u = model.rvar(N)           

    z_set = (abs(z) <= u, u <= 1)
    model.min(k)
    model.st(c @ x >= tau)
    model.st(((w + z*delta) @ x - b <= k*u.sum()).forall(z_set))
    model.st(k >= 0)

    #model.solve(grb, display=False) # disable solution message
    model.solve(ecos, display=False) # disable solution message

    return model.get(), x.get()     # the optimal objective and solution


def sim(x_sol, zs):
    """
    The function sim is for calculating the probability of violation
    via simulations.
        x_sol: solution of the Knapsack problem
        zs: random sample of the random variable z
    """

    ws = w + zs*delta   # random samples of uncertain weights

    return (ws @ x_sol > b).mean()

step = 0.1
rs = np.arange(1, 5+step, step)         # all budgets of uncertainty
num_samp = 20000
zs = 1-2*rd.rand(num_samp, N)           # random samples for z

# Start measuring time 20241128
start_time = time.time()

"""Robust optimization"""
outputs_rb = [robust(r) for r in rs]
targets = [output[0]
           for output in outputs_rb]    # RO objective as targets
pv_rb = [sim(output[1], zs)
         for output in outputs_rb]      # probability of violations

#20241119
print("Robust optimization={}".format(pv_rb))


"""Robustness optimization"""
outputs_rbn = [robustness(target)
               for target in targets]   
pv_rbn = [sim(output[1], zs)
          for output in outputs_rbn]    # probability of violations

#20241128
print("Robustness optimization={}".format(pv_rbn))

# End measuring time 20241128
end_time = time.time()

# Print the processing time
print(f"Processing time: {end_time - start_time:.4f} seconds")

plt.plot(rs, pv_rb, marker='o', markersize=5, c='b',
         label='Robust Optimization')
plt.plot(rs, pv_rbn, c='r',
         label='Robustness Optimization')

plt.legend()
plt.xlabel('Parameter r in robust optimization')
plt.ylabel('Prob. violation')
plt.show()

plt.scatter(targets, pv_rb, c='b', alpha=0.3,
            label='Robust Optimization')
plt.scatter(targets, pv_rbn, c='r', alpha=0.3,
            label='Robustness Optimization')

plt.legend()
plt.xlabel(r'Target return $\tau$')
plt.ylabel('Prob. violation')
plt.show()





