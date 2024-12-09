import picos as pic
P = pic.Problem()
y = pic.RealVariable("y",2)
z = pic.RealVariable("z",3)
a = {}
a[0] = pic.Constant("a[0]",[-1,-1,0])
a[1] = pic.Constant("a[1]",[0,0,-2])
c = pic.Constant("c",[1,-1,0])
b = pic.Constant("b",[-1,0])
P.add_constraint(z == c - y[0]*a[0] - y[1]*a[1])
P.set_objective('max',b|y)
P.add_constraint(abs(z[1:]) <= z[0])
P.options.verbosity = 1
solution = P.solve()
print("status:", solution.claimedStatus)
print("optional value:", P.value)
print("optional solution")
print("y:")
print(y.value)