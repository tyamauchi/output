import picos as pic
pb=pic.Problem()
x=pic.RealVariable("x",3)
pb.add_constraint( x[0]+2*x[1]+2*x[2] <= 10 )
pb.add_constraint( 3*x[0]+x[2] <= 11 )
pb.add_constraint( 4*x[0]+3*x[1]+2*x[2] <= 20 )
pb.add_constraint( x[0]>=abs(x[1:3]) )
pb.set_objective("min",x[0]+2*x[1]+3*x[2])
solution=pb.solve()
print("終了状態:",solution.claimedStatus)
print("目的関数値:",round(pb.value,2))
print("最適解:",solution.primals)
# 追加
for i in range(3):
    print(f"x[{i}] = {round(solution.primals[x][i, 0], 2)}")