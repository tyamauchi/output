import pulp
import numpy as np

# 問題の定義
MN = 4
Nodes = [1, 2, 3, 4]  # s, a, b, t
Edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]

# 隣接リストの作成
Ng_plus, Ng_minus = {k: [] for k in Nodes}, {k: [] for k in Nodes}
for (u, v) in Edges:
    Ng_plus[u].append(v)
    Ng_minus[v].append(u)

# コストと容量の定義
C = {(1, 2): 2, (1, 3): 6, (2, 3): 1, (2, 4): 5, (3, 4): 3}
U = {(1, 2): 0, (1, 3): 2, (2, 3): 9, (2, 4): 9, (3, 4): 5}
maxU = 10

def relax_solve(lmbda=None, s=1, t=4):
    if lmbda is None:
        lmbda = np.zeros(MN+1) 
    
    model = pulp.LpProblem("RelaxSolve", pulp.LpMinimize)
    
    # 変数の定義
    x = {(u, v): pulp.LpVariable(f"x_{u}_{v}", cat=pulp.LpBinary) for (u, v) in Edges}
    
    # 目的関数
    obj = sum(x[u, v] * C[u, v] for (u, v) in Edges)
    obj += lmbda[s-1] * (1 - sum(x[s, u] for u in Ng_plus[s]))  # 1式目
    obj += lmbda[t-1] * (-1 + sum(x[u, t] for u in Ng_minus[t]))  # 2式目
    for n in Nodes:
        if n == s or n == t:
            continue
        iterm = sum(x[u, n] for u in Ng_minus[n])
        oterm = sum(x[n, u] for u in Ng_plus[n])
        obj += lmbda[n-1] * (-oterm + iterm)
    
    model += obj
    
    # 制約条件
    model += sum(x[u, v] * U[u, v] for (u, v) in Edges) <= maxU
    
    # 最適化実行
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    
    # 劣勾配ベクトルの計算
    dvg = np.zeros(MN+1) 
    dvg[s-1] = 1 - sum(pulp.value(x[s, u]) for u in Ng_plus[s])
    dvg[t-1] = -1 + sum(pulp.value(x[u, t]) for u in Ng_minus[t])
    for n in Nodes:
        if n == s or n == t:
            continue
        iterm = sum(pulp.value(x[u, n]) for u in Ng_minus[n])
        oterm = sum(pulp.value(x[n, u]) for u in Ng_plus[n])
        dvg[n-1] = iterm - oterm
    
    return pulp.value(model.objective), dvg

lmbda = np.zeros(MN+1) 
i, epsilon, max_iter = 1, 0.001, 2000

while i <= max_iter:
    _, df = relax_solve(lmbda=lmbda, s=1, t=4)
    if i % 25 == 0:
        print(f"{i}\t {lmbda}")
    
    if all(abs(df[v] / i) <= epsilon for v in range(MN)):
        print("end", lmbda)
        break
    
    lmbda += df / i  # ベクトルの更新
    i += 1

obj, _ = relax_solve(lmbda=lmbda, s=1, t=4)
print(obj)
