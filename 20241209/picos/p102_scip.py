import pyscipopt as scip

model = scip.Model()

s = model.addVar(name="s", vtype="C")  # 実数変数
t = model.addVar(name="t", vtype="C")  # 実数変数

model.addCons(s >= t**2)  # s >= t^2

model.setObjective(s, sense="minimize")

model.optimize()

# 結果を取得
if model.getStatus() == "optimal":
    print("Optimal value:")
    print("s:", model.getVal(s), "t:", model.getVal(t))
else:
    print("Solution not optimal or no solution found.")
