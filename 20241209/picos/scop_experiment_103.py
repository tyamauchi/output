import picos as pic
import time      # 20241209

P = pic.Problem()
y = pic.RealVariable("y",2)
z = pic.RealVariable("z",3)
a = {}
a[0] = pic.Constant("a[0]",[-1,-1,0])
a[1] = pic.Constant("a[1]",[0,0,-2])
c = pic.Constant("c",[1,-1,0])
b = pic.Constant("b",[-1,0])
P.add_constraint(z == c - y[0]*a[0] - y[1]*a[1])

#P.options.solver = "cvxopt"      # cvxopt
#P.options.solver = "gurobi"      # gurobi
#P.options.solver = "scip"      # scip
P.options.solver = "qics"      # qics
#P.options.solver = "ecos"      # ecos
P.options.verbosity = 1  

P.set_objective('max',b|y)
P.add_constraint(abs(z[1:]) <= z[0])
P.options.verbosity = 1

# Start measuring time 20241209
start_time = time.time()

solution = P.solve()

# End measuring time 20241209
end_time = time.time()
print(f"Processing time: {end_time - start_time:.4f} seconds")

print("status:", solution.claimedStatus)
print("optional value:", P.value)
print("optional solution")
print("y:")
print(y.value)
# 追加
#if P.options.solver == "gurobi":
#    for i in range(3):
#        print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")