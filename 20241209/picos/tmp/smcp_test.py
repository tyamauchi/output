from smcp import SDP
import numpy as np

# 行列の定義
C = np.array([[1, 0], [0, 1]])  # 目的関数のコスト行列
A1 = np.array([[1, 0], [0, 0]])  # 制約1の係数行列
A2 = np.array([[0, 0], [0, 1]])  # 制約2の係数行列
b = [1, 1]  # 制約の右辺

# SDP問題の設定
problem = SDP()

# 半正定値変数 X を追加
X = problem.add_variable("X", (2, 2), "symmetric")

# 目的関数: minimize trace(CX)
problem.set_objective("min", C @ X)

# 制約: trace(A1 * X) <= b[0]
problem.add_constraint(np.trace(A1 @ X) <= b[0])

# 制約: trace(A2 * X) <= b[1]
problem.add_constraint(np.trace(A2 @ X) <= b[1])

# 制約: X は半正定値
problem.add_psd_constraint(X)

# 問題を解く
result = problem.solve()

# 結果の表示
print("Optimal Value:", result["obj_value"])
print("Optimal Solution X:")
print(result["X"])
