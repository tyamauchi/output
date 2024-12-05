import picos as pic
P = pic.Problem()
s = pic.RealVariable("s",1)
t = pic.RealVariable("t",1)
P.add_constraint(s >= t**2)
P.set_objective("min", s)
P.options.verbosity = 1
solution = P.solve()
print("status:",solution.claimedStatus)
print("optional value:", P.value)
print("optional solution")
print("s:", s.value, "t:", t.value)
