import csv 
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('data.csv')
df = df.loc[df['student_id']=='TRL_zny']
print(df.groupby('student_id')['attempt'].mean())
graph = go.Figure(go.Bar(
   x = df.groupby('level')['attempt'].mean(),
   y = ['level1','level2','level3','level4'],
   orientation = 'h'
))
graph.show()