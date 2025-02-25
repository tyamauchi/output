from pulp import *
m = LpProblem(sense=LpMaximize) # 数理モデル
x,y,z = [LpVariable(c,cat=LpBinary) for c in 'xyz'] # 変数
m += lpDot([7,8,9], [x,y,z]) # 目的関数
m += lpDot([6,7,8], [x,y,z]) <= 14 # 制約条件
m.solve() # 求解
print([value(v) for v in [x,y,z]]) # 出力
#>>>
#[1.0, 0.0, 1.0]
