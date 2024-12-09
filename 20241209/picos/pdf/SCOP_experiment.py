import picos as pic
import time      # 20241209

pb=pic.Problem()
x=pic.RealVariable("x",3)
pb.add_constraint( x[0]+2*x[1]+2*x[2] <= 10 )
pb.add_constraint( 3*x[0]+x[2] <= 11 )
pb.add_constraint( 4*x[0]+3*x[1]+2*x[2] <= 20 )
pb.add_constraint( x[0]>=abs(x[1:3]) )
pb.set_objective("min",x[0]+2*x[1]+3*x[2])

#pb.options.solver = "cvxopt"      # cvxopt
#pb.options.solver = "gurobi"      # gurobi
#pb.options.solver = "scip"      # scip
#pb.options.solver = "qics"      # qics
pb.options.solver = "ecos"      # ecos
pb.options.verbosity = 1

# Start measuring time 20241209
start_time = time.time()

solution=pb.solve()

# End measuring time 20241209
end_time = time.time()
print(f"Processing time: {end_time - start_time:.4f} seconds")

print("終了状態:",solution.claimedStatus)
print("目的関数値:",round(pb.value,2))
print("最適解:",solution.primals)
# 追加
if pb.options.solver == "gurobi":
    for i in range(3):
        print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")