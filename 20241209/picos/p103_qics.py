import picos as pic

# Create a PICOS problem instance
P = pic.Problem()

# Define variables
y = pic.RealVariable("y", 2)  # Real variable y with dimension 2
z = pic.RealVariable("z", 3)  # Real variable z with dimension 3

# Define constants
a = {}
a[0] = pic.Constant("a[0]", [-1, -1, 0])
a[1] = pic.Constant("a[1]", [0, 0, -2])
c = pic.Constant("c", [1, -1, 0])
b = pic.Constant("b", [-1, 0])

# Add constraints
P.add_constraint(z == c - y[0] * a[0] - y[1] * a[1])
P.add_constraint(abs(z[1:]) <= z[0])

# Set the objective function
P.set_objective("max", b | y)

# Specify QICS as the solver
P.options.solver = "qics"
P.options.verbosity = 1  # Enable detailed solver output

# Solve the problem
solution = P.solve()

# Display the results
print("status:", solution.claimedStatus)
print("optimal value:", P.value)
print("optimal solution")
print("y:")
print(y.value)
