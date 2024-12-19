from pulp import LpProblem, LpMaximize, LpVariable, LpStatus

# 問題の定義
problem = LpProblem(name="linear-programming", sense=LpMaximize)

# 変数の定義
#theta = LpVariable(name="theta", lowBound=None)

dx1 = LpVariable(name="dx1", lowBound=0)
dx2 = LpVariable(name="dx2", lowBound=0)
dx3 = LpVariable(name="dx3", lowBound=0)
dy1 = LpVariable(name="dy1", lowBound=0)
dy2 = LpVariable(name="dy2", lowBound=0)
lambda1 = LpVariable(name="lambda1", lowBound=0)
lambda2 = LpVariable(name="lambda2", lowBound=0)
lambda3 = LpVariable(name="lambda3", lowBound=0)
lambda4 = LpVariable(name="lambda4", lowBound=0)
lambda5 = LpVariable(name="lambda5", lowBound=0)
lambda6 = LpVariable(name="lambda6", lowBound=0)

# 目的関数
#problem += theta, "Objective"

problem += (dx1 + dx2 + dx3) + (dy1 + dy2), "Objective"

# 制約条件
problem += dx1 == 40*1  -   (40 *  lambda1 + 20 *  lambda2 + 15 * lambda3 + 30 *  lambda4 + 20 *  lambda5 + 16 * lambda6) , "Constraint 1"
problem += dx2 == 0.8 * 1 - (0.8 * lambda1 + 0.2 * lambda2 +      lambda3 + 0.5 * lambda4 + 0.9 * lambda5 +      lambda6) , "Constraint 2"
problem += dx3 == 1       - (      lambda1 + 0.9 * lambda2 + 0.8 *lambda3 + 0.9 * lambda4 +       lambda5 +      lambda6) , "Constraint 3"

problem += dy1 == 40 * lambda1 + 60 * lambda2 + 30 * lambda3 + 20 * lambda4 + 70 * lambda5 + 50 * lambda6 - 40, "Constraint 4"
problem += dy2 == 30 * lambda1 + 90 * lambda2 + 55 * lambda3 + 70 * lambda4 + 24 * lambda5 + 60 * lambda6 - 30, "Constraint 5"

# 解を求める
status = problem.solve()

# 結果の表示
print(f"Status: {problem.status}, {LpStatus[problem.status]}")
#print(f"Optimal theta: {theta.value()}")
print(f"Optimal theta: {(dx1.value() + dx2.value() + dx3.value()) + (dy1.value() + dy2.value())}")
print(f"dx1: {dx1.value()}")
print(f"dx2: {dx2.value()}")
print(f"dx3: {dx3.value()}")
print(f"dy1: {dy1.value()}")
print(f"dy2: {dy2.value()}")
print(f"lambda1: {lambda1.value()}")
print(f"lambda2: {lambda2.value()}")
print(f"lambda3: {lambda3.value()}")
print(f"lambda4: {lambda4.value()}")
print(f"lambda5: {lambda5.value()}")
print(f"lambda6: {lambda6.value()}")
