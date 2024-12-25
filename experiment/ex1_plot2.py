import pandas as pd
import matplotlib.pyplot as plt

# データフレームの作成
#df = pd.DataFrame(
#    {
#        "employee": [50, 70, 30, 45, 50],
#        "cost": [110, 80, 120, 90, 210], 
#        "profit": [300, 250, 270, 200, 400]
#    }
#)

# 理想の値   Dの値を変更する。実効値が1になる。
df = pd.DataFrame(
    {
        "employee": [50, 70, 30, 36.09, 50],
        "cost": [110, 80, 120, 72.2, 210], 
        "profit": [300, 250, 270, 200, 400]}
)

# x軸とy軸のデータを計算
df["input1/output"] = df["employee"] / df["profit"]
df["input2/output"] = df["cost"] / df["profit"]

# グラフの描画
plt.figure(figsize=(8, 6))
plt.scatter(df["input1/output"], df["input2/output"], color="blue", alpha=0.7)

# 軸ラベルとタイトルを設定
plt.xlabel("Input1/Output (Employee/Profit)")
plt.ylabel("Input2/Output (Cost/Profit)")
plt.title("Scatter Plot of Inputs to Output Ratios")

# データポイントのラベルを追加
for i, (x, y) in enumerate(zip(df["input1/output"], df["input2/output"])):
    plt.text(x, y, f"DMU {i+1}", fontsize=9, ha="right")

# グリッドを追加
plt.grid(alpha=0.3)

# グラフを表示
plt.show()
