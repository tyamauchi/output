from rsome import ro
#import rsome.grb_solver as grb
import rsome.eco_solver as eco   #20241224
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time      # 20241225

# Parameters of the lot-sizing problem
#N = 30
#c = 20
#dmax = 20
#---20241224---
N = 10
c = 20
dmax = 20
#---20241224---

Gamma = 20*np.sqrt(N)
xy = 10*rd.rand(2, N)
t = ((xy[[0]] - xy[[0]].T) ** 2
     + (xy[[1]] - xy[[1]].T) ** 2) ** 0.5

model = ro.Model()          # define a model
x = model.dvar(N)           # define location decisions
y = model.ldr((N, N))       # define decision rule as the shifted quantities
d = model.rvar(N)           # define random variables as the demand

y.adapt(d)                  # the decision rule y affinely depends on d

uset = (d >= 0,
        d <= dmax,
        sum(d) <= Gamma)    # define the uncertainty set

# define model objective and constraints
model.minmax((c*x).sum() + (t*y).sum(), uset)
model.st(d <= y.sum(axis=0) - y.sum(axis=1) + x)
model.st(y >= 0)
model.st(x >= 0)
model.st(x <= 20)

# Start measuring time 20241225
start_time = time.time()
model.solve(eco)

# End measuring time 20241128
end_time = time.time()

# Print the processing time
print(f"Processing time: {end_time - start_time:.4f} seconds")

plt.figure(figsize=(5, 5))
plt.scatter(xy[0], xy[1], c='w', edgecolors='k')
plt.scatter(xy[0], xy[1], s=40*x.get(), c='k', alpha=0.6)
plt.axis('equal')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.grid()
plt.show()