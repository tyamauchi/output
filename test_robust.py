import numpy as np

# 定数を定義
w = np.array([2, 3, 5])
delta = np.array([0.5, 0.2, 0.3])
b = 10

# 解とランダムサンプルを定義
x_sol = np.array([1, 0, 1])
zs = np.random.normal(0, 1, (1000, 3))  # 1000個のサンプルを生成

# 関数定義
def sim(x_sol, zs):
    """
    Calculate the probability of violation via simulations.
    """
    ws = w + zs * delta  # 不確実な重みを計算
    print("ws={}".format(ws))
    return (ws @ x_sol > b).mean()

# 実行
print("x_sol={} zs={}".format(x_sol, zs))
violation_probability = sim(x_sol, zs)
print(f"制約違反の確率: {violation_probability:.2%}")
