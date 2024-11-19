import numpy as np

# サンプルデータ
ws = np.array([[3, 4], [5, 6], [7, 8]])
x_sol = np.array([1, 0])  # アイテム選択
b = 4  # 制約値

# 制約違反の確率
violation_probability = (ws @ x_sol > b).mean()
print(f"制約違反の確率: {violation_probability:.2%}")