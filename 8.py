import plotly.graph_objects as go
import pandas as pd
tips = pd.read_csv("./DataSet/tips.csv")
fig = go.Figure()
Scatter = go.Scatter3d(
    x = tips['total_bill'],
    y = tips['tip'],
    z = tips['size'],
    mode = 'markers'
)
fig.add_trace(Scatter)
fig.update_layout(scene = dict(xaxis_title = 'Total Bill',yaxis_title = 'Tip',zaxis_title = 'Size'))
fig.update_layout(title = '3D Scatter plot with Tips Dataset')
fig.write_html("./Externals/8.html")