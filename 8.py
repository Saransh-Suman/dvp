import plotly.express as px
import pandas as pd

df = pd.read_csv("./DataSet/tips.csv")
fig = px.scatter_3d(df, x='total_bill', y='tip', z='size', 
                    title='3D Scatter plot with Tips Dataset',
                    labels={'total_bill': 'Total Bill', 'tip': 'Tip', 'size': 'Size'})

fig.write_html("./Externals/8.html")
