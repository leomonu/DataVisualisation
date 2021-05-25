import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
studentId = input('Enter Student Id :')
studentDf = df.loc[df["student_id"]==studentId]
print(studentDf.groupby("level")["attempt"].mean())

fig  = go.Figure(go.Bar(
                 x = studentDf.groupby("level")["attempt"].mean(),
                 y = ["Level 1","Level 2","Level 3","Level 4"],
                 orientation = "h"

))
fig.show()