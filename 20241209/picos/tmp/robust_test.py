import cvxopt as cvx 
import picos as pic
import time      # 20241209

A=pic.Constant("A",cvx.matrix([-1,3,0,-3,3,3,3,0,0,0,2,-5 ],(4,3)))
b=pic.Constant("b",cvx.matrix([7,3,6,-5],(4,1))) 
c=pic.Constant("c",cvx.matrix([-4,9,3],(3,1))) 
P=[cvx.matrix([1,0,0,0,3,0,0,0,1],(3,3)), 
   cvx.matrix([2,0,0,0,1,0,0,0,2],(3,3)), 
   cvx.matrix([2,0,0,0,0.5,0,0,0,1],(3,3)), 
   cvx.matrix([1,0,0,0,2,0,0,0,1],(3,3))]
prob = pic.Problem()
x = pic.RealVariable ("x",3) 
prob.add_list_of_constraints([abs(P[i]*x)<=b[i]-A[i,:]*x for i in range(4)])
prob.add_list_of_constraints([x[i]>=0 for i in range(3)]) 
objective=c|x

#prob.options.solver = "cvxopt"      # cvxopt
#prob.options.solver = "gurobi"      # gurobi
#prob.options.solver = "scip"      # scip
#prob.options.solver = "qics"      # qics
#prob.options.solver = "ecos"      # ecos
prob.options.solver = "smcp"      # gurobi
prob.options.verbosity = 1

# Start measuring time 20241209
start_time = time.time()

prob.set_objective("min",objective)
solution = prob.solve()

# End measuring time 20241209
end_time = time.time()
print(f"Processing time: {end_time - start_time:.4f} seconds")

print("status:", solution.claimedStatus)
print("objective value:", prob.value) 
print(solution.primals)
# 追加
if prob.options.solver == "gurobi":
    for i in range(3):
        print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")