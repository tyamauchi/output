import picos as pic
import time      # 20241209

P = pic.Problem()
s = pic.RealVariable("s",1)
t = pic.RealVariable("t",1)
P.add_constraint(s >= t**2)

#P.options.solver = "cvxopt"      # cvxopt
#P.options.solver = "gurobi"      # gurobi
#P.options.solver = "scip"      # scip
#P.options.solver = "qics"      # qics
P.options.solver = "ecos"      # ecos

P.options.verbosity = 1

P.set_objective("min", s)
P.options.verbosity = 1

# Start measuring time 20241209
start_time = time.time()
solution = P.solve()

# End measuring time 20241209
end_time = time.time()
print(f"Processing time: {end_time - start_time:.4f} seconds")

print("status:",solution.claimedStatus)
print("optional value:", P.value)
print("optional solution")
print("s:", s.value, "t:", t.value)
# 追加
#if P.options.solver == "gurobi":
#    for i in range(3):
#        print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")
