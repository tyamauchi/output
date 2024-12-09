from gurobipy import Model, GRB, quicksum

# パラメータ設定
nodes = ["s", "a", "b", "c", "t"]  # ノード
edges = [("s", "a"), ("s", "b"), ("a", "c"), ("b", "c"), ("a", "t"), ("c", "t"), ("b", "t")]  # リンク
costs = {("s", "a"): 4, ("s", "b"): 2, ("a", "c"): 3, ("b", "c"): 1,
         ("a", "t"): 6, ("c", "t"): 5, ("b", "t"): 8}  # コスト
delays = {("s", "a"): 10, ("s", "b"): 15, ("a", "c"): 20, ("b", "c"): 5,
          ("a", "t"): 25, ("c", "t"): 30, ("b", "t"): 35}  # 基本遅延
uncertainties = {("s", "a"): 5, ("s", "b"): 3, ("a", "c"): 8, ("b", "c"): 2,
                 ("a", "t"): 10, ("c", "t"): 7, ("b", "t"): 9}  # 遅延の変動幅
budget = 15  # コスト制約

# モデル作成
model = Model("NetworkDelayRobustOptimization")

# 変数定義
x = model.addVars(edges, vtype=GRB.BINARY, name="x")  # 使用するか
u = model.addVars(edges, vtype=GRB.CONTINUOUS, name="u")  # 遅延増加分

# 目的関数：平均遅延（ロバスト性を考慮）
model.setObjective(
    quicksum(x[e] * (delays[e] + u[e]) for e in edges), GRB.MINIMIZE
)

# 制約1: コスト制約
model.addConstr(quicksum(x[e] * costs[e] for e in edges) <= budget, name="Cost")

# 制約2: パス制約（フロー制約）
for node in nodes:
    if node == "s":
        model.addConstr(quicksum(x[e] for e in edges if e[0] == node) - 
                        quicksum(x[e] for e in edges if e[1] == node) == 1, name=f"Flow_{node}")
    elif node == "t":
        model.addConstr(quicksum(x[e] for e in edges if e[0] == node) - 
                        quicksum(x[e] for e in edges if e[1] == node) == -1, name=f"Flow_{node}")
    else:
        model.addConstr(quicksum(x[e] for e in edges if e[0] == node) - 
                        quicksum(x[e] for e in edges if e[1] == node) == 0, name=f"Flow_{node}")

# 制約3: 不確実性制約
for e in edges:
    model.addConstr(u[e] <= uncertainties[e] * x[e], name=f"Uncertainty_{e}")

# 最適化実行
model.optimize()

# 結果出力
if model.status == GRB.OPTIMAL:
    print(f"最適目的関数値: {model.objVal}")
    print("使用されるリンク:")
    for e in edges:
        if x[e].x > 0.5:  # バイナリ変数のため
            print(f"  {e}: 遅延 = {delays[e] + u[e].x:.2f}")
else:
    print("最適解が見つかりませんでした。")
