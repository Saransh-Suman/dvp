import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.layouts import gridplot

# Load the tips dataset (Ensure the file exists in your directory)
tips = pd.read_csv("./DataSet/tips.csv") 
output_file("bokeh_tips_plots.html")

# Output to static HTML file 

# --- 1. Histogram ---
hist, edges = np.histogram(tips['total_bill'], bins=8)
hist_plot = figure(title="Histogram of Total Bill", x_axis_label='Total Bill', y_axis_label='Frequency')
hist_plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", line_color="white")

# --- 2. Bar Plot ---
# We need strings for the x_range in a bar plot
day_categories = list(tips['day'].unique())
average_total_bill = tips.groupby('day')['total_bill'].mean()
bar_plot = figure(title="Average Total Bill per Day", x_axis_label='Day', y_axis_label='Average Total Bill', x_range=day_categories)
bar_plot.vbar(x=day_categories, top=average_total_bill, width=0.5, color="orange")

# --- 3. Scatter Plot ---
# Using ColumnDataSource is best practice for mapping DataFrame columns
source = ColumnDataSource(tips)
scatter_plot = figure(title="Scatter Plot of Total Bill vs Tip", x_axis_label='Total Bill', y_axis_label='Tip')
scatter_plot.scatter(x='total_bill', y='tip', size=8, color="green", alpha=0.6, source=source)

# Combine plots into a grid
plots = gridplot([[hist_plot, bar_plot], [scatter_plot]])

# Show the combined plot
show(plots)