import plotly.express as px 
import pandas as pd
# Load the dataset (replace 'your_dataset.csv' with the actual file path) data = pd.read_csv("Rainfall_data.csv")
# Combine Year, Month, and Day columns to create a datetime column data['Date'] = pd.to_datetime(data[['Year', 'Month', 'Day']])
# Create time series plot
data = pd.read_csv("./DataSet/Rainfall_data.csv")
data['Date'] = pd.to_datetime(data[['Year','Month','Day']])
fig = px.line(data, x='Date', y=[ 'Temperature'],
title='Time Series Plot', labels={'value': 'Values'}, line_shape='linear') 
fig.show()