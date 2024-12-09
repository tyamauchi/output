from pyscipopt import Model

# モデル作成
model = Model("Knapsack Problem")

# データ定義
weights = [2, 3, 4, 5]  # 各アイテムの重量
values = [3, 4, 5, 6]   # 各アイテムの価値
capacity = 10           # ナップサックの最大重量
n_items = len(weights)  # アイテムの数

# 変数を追加 (0-1変数: アイテムを選ぶかどうか)
x = [model.addVar(name=f"x[{i}]", vtype="B") for i in range(n_items)]

# 制約: 重量の合計はナップサックの容量を超えない
model.addCons(sum(weights[i] * x[i] for i in range(n_items)) <= capacity, name="WeightConstraint")

# 目的関数: 価値の合計を最大化
model.setObjective(sum(values[i] * x[i] for i in range(n_items)), sense="maximize")

# 問題を解く
model.optimize()

# 結果を出力
status = model.getStatus()
if status == "optimal":
    print("Status:", status)
    print("Optimal Value:", model.getObjVal())
    print("Selected Items:")
    for i in range(n_items):
        print(f"x[{i}] = {model.getVal(x[i])}")
else:
    print("Solution not optimal or no solution found.")
