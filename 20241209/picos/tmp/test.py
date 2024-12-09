from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# グラフの定義
nodes = ['s', 'a', 'b', 'c', 't']
edges = {
    ('s', 'a'): 2,
    ('s', 'b'): 4,
    ('a', 'b'): 1,
    ('a', 'c'): 7,
    ('b', 'c'): 3,
    ('b', 't'): 6,
    ('c', 't'): 2
}

# 問題の定義
problem = LpProblem("Shortest_Path", LpMinimize)

# 変数の定義
x = LpVariable.dicts("x", edges.keys(), 0, 1, cat='Binary')

# 目的関数
problem += lpSum(edges[edge] * x[edge] for edge in edges), "Total Cost"

# 制約: ソースノードからのフロー
problem += lpSum(x[edge] for edge in edges if edge[0] == 's') == 1, "Source_Flow"

# 制約: ディスティネーションノードへのフロー
problem += lpSum(x[edge] for edge in edges if edge[1] == 't') == 1, "Destination_Flow"

# 制約: 中間ノードのフロー保存則
for node in nodes:
    if node not in ['s', 't']:
        problem += (
            lpSum(x[edge] for edge in edges if edge[0] == node) == 
            lpSum(x[edge] for edge in edges if edge[1] == node),
            f"Flow_Conservation_{node}"
        )

# 問題を解く
problem.solve()

# 結果の表示
print("Status:", problem.status)
print("Objective Value (Total Cost):", problem.objective.value())
for edge in edges:
    if x[edge].value() > 0:
        print(f"Edge {edge} is in the path with value {x[edge].value()}")
