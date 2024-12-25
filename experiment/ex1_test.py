from Pyfrontier.frontier_model import EnvelopDEA
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.DataFrame(
#    {
#        "employee": [50, 70, 30, 45, 50],
#        "cost": [110, 80, 120, 90, 210], 
#        "profit": [300, 250, 270, 200, 400]}
#)

# 理想の値   Dの値を変更する。実効値が1になる。
df = pd.DataFrame(
    {
        "employee": [50, 70, 30, 36.09, 50],
        "cost": [110, 80, 120, 72.2, 210], 
        "profit": [300, 250, 270, 200, 400]}
)

dea = EnvelopDEA("CRS", "in")
dea.fit(df[["employee", "cost"]].to_numpy(), df[["profit"]].to_numpy())
dea.results
print(dea.results)

