from pulp import LpProblem, LpMinimize, LpVariable, LpStatus

# 問題の定義
problem = LpProblem(name="linear-programming", sense=LpMinimize)

# 変数の定義
theta = LpVariable(name="theta", lowBound=None)
lambda1 = LpVariable(name="lambda1", lowBound=0)
lambda2 = LpVariable(name="lambda2", lowBound=0)
lambda3 = LpVariable(name="lambda3", lowBound=0)
lambda4 = LpVariable(name="lambda4", lowBound=0)
lambda5 = LpVariable(name="lambda5", lowBound=0)
lambda6 = LpVariable(name="lambda6", lowBound=0)

# 目的関数
problem += theta, "Objective"

# 制約条件
problem += 3 * theta - (3 * lambda1 + 5 * lambda2 + 6 * lambda3 + 3 * lambda4 + 2 * lambda5 + 16 * lambda6) >= 0, "Constraint 1"
problem += 2 * theta - (2 * lambda1 + 5 * lambda2 + 3 * lambda3 + 3 * lambda4 + 8 * lambda5 + 4 * lambda6) >= 0, "Constraint 2"
problem += 6 * lambda1 + 10 * lambda2 + 12 * lambda3 + 9 * lambda4 + 8 * lambda5 + 16 * lambda6 - 6 >= 0, "Constraint 3"

# 解を求める
status = problem.solve()

# 結果の表示
print(f"Status: {problem.status}, {LpStatus[problem.status]}")
print(f"Optimal theta: {theta.value()}")
print(f"lambda1: {lambda1.value()}")
print(f"lambda2: {lambda2.value()}")
print(f"lambda3: {lambda3.value()}")
print(f"lambda4: {lambda4.value()}")
print(f"lambda5: {lambda5.value()}")
print(f"lambda6: {lambda6.value()}")
