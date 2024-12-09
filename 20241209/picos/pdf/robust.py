import cvxopt as cvx 
import picos as pic
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
prob.set_objective("min",objective)
solution = prob.solve()
print("status:", solution.claimedStatus)
print("objective value:", prob.value) 
print(solution.primals)
# 追加
for i in range(3):
    print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")