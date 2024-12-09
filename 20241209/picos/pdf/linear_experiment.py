from pulp import *
prob = LpProblem("ex1",LpMinimize)
x1 = LpVariable("x1", lowBound=0,cat=LpContinuous)
x2 = LpVariable("x2", lowBound=0,cat=LpContinuous)
prob += 2*x1 + 3*x2
prob += 3*x1 + 4*x2 >= 1

#prob.options.solver = "cvxopt"      # cvxopt
#prob.options.solver = "gurobi"      # gurobi
#prob.options.solver = "scip"      # scip
#prob.options.solver = "qics"      # qics
#prob.options.solver = "ecos"      # ecos
#prob.options.verbosity = 1

print(prob)
status = prob.solve()
print("終了状態:",LpStatus[status])
print("目的関数値:",value(prob.objective))
for var in prob.variables():
    print(var.name,":",var.varValue)
