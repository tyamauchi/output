import picos as pic

# Create a PICOS problem instance
P = pic.Problem("QCQP Example")

# Define the variables
x1 = pic.RealVariable("x1", 1)
x2 = pic.RealVariable("x2", 1)

# Define the objective function
P.set_objective("max", x1 + 2 * x2)

# Add quadratic constraints
P.add_constraint(x1**2 + x2**2 <= 1)  # Circle constraint
P.add_constraint(x1 - x2 <= 0.5)      # Linear constraint

# Specify SCIP as the solver
P.options.solver = "scip"
P.options.verbosity = 1

# Solve the problem
solution = P.solve()

# Display results
print("Solver Status:", solution.claimedStatus)
print("Optimal Value:", P.value)
print("Optimal Solution:")
print(f"x1 = {x1.value}")
print(f"x2 = {x2.value}")
