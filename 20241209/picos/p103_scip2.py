import picos as pic

P = pic.Problem()

# 変数の定義
y = pic.RealVariable("y", 2)  # 2次元の実数変数 y
z = pic.RealVariable("z", 3)  # 3次元の実数変数 z

# 定数を定義
a = {}
a[0] = pic.Constant("a[0]", [-1, -1, 0])
a[1] = pic.Constant("a[1]", [0, 0, -2])
c = pic.Constant("c", [1, -1, 0])
b = pic.Constant("b", [-1, 0])

# 制約: z = c - y[0]*a[0] - y[1]*a[1]
P.add_constraint(z == c - y[0]*a[0] - y[1]*a[1])

# 目的関数: max b | y
P.set_objective('max', b | y)

# 制約: abs(z[1:]) <= z[0] を2つの制約に分解
P.add_constraint(z[1] <= z[0])
P.add_constraint(-z[1] <= z[0])
P.add_constraint(z[2] <= z[0])
P.add_constraint(-z[2] <= z[0])

# ソルバーをSCIPに設定
P.options.solver = "scip"  # SCIPを使用

# 解法の詳細を出力する
P.options.verbosity = 1

# 問題を解く
solution = P.solve()

# 解を表示
print("status:", solution.claimedStatus)
print("optional value:", P.value)
print("optimal solution")
print("y:", y.value)
