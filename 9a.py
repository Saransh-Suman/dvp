import pandas as pd
import plotly.express as px

# 1. Load data
df = pd.read_csv("./DataSet/Rainfall_data.csv")

# 2. Convert to Date
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# 3. Plot and Show
px.line(df, x='Date', y='Temperature', title='Time Series').show()
