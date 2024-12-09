import picos as pic
import cvxopt as cvx
import time      # 20241209

A = cvx.matrix([-1,3,0,-3,3,3,3,0,0,0,2,-5],(4,3))
b = cvx.matrix([5,4,6,-4],(4,1))
c = cvx.matrix([-3,11,2],(3,1))
#print(A)
#print(b)
#print(c)

A = pic.Constant("A",A)
b = pic.Constant("b",b)
c = pic.Constant("c",c)

P = []
P.append(cvx.matrix([1,0,0,0,2,0,0,0,1],(3,3)))
P.append(cvx.matrix([2,0,0,0,1,0,0,0,2],(3,3)))
P.append(cvx.matrix([1,0,0,0,0.5,0,0,0,1],(3,3)))
P.append(cvx.matrix([1,0,0,0,3,0,0,0,1],(3,3)))
for i in range(len(P)):
    P[i] = pic.Constant("P["+str(i)+"]",P[i])


prob = pic.Problem()
x = pic.RealVariable("x",3)
prob.add_constraint(abs(P[0]*x) <= b[0] - A[0,:]*x)
prob.add_constraint(abs(P[1]*x) <= b[1] - A[1,:]*x)
prob.add_constraint(abs(P[2]*x) <= b[2] - A[2,:]*x)
prob.add_list_of_constraints([x[i] >= 0 for i in range(3)])
objective = -3*x[0] + 11*x[1] + 2*x[2]
prob.set_objective('min',objective)

#prob.options.solver = "cvxopt"      # cvxopt
#prob.options.solver = "gurobi"      # gurobi
#prob.options.solver = "scip"      # scip
#prob.options.solver = "qics"      # qics
prob.options.solver = "ecos"      # ecos

prob.options.verbosity = 1

# Start measuring time 20241209
start_time = time.time()

solution = prob.solve()

# End measuring time 20241209
end_time = time.time()
print(f"Processing time: {end_time - start_time:.4f} seconds")

print("status:", solution.claimedStatus)
print("optional value:", prob.value)
print("optional solution")
print("x:")
print(x.value)
# 追加
if prob.options.solver == "gurobi":
    for i in range(3):
        print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")