import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

df = pd.read_csv("./DataSet/tips.csv")

# 1. Histogram (Manual binning is required in Bokeh)
hist, edges = np.histogram(df['total_bill'], bins=8)
p1 = figure(title="Total Bill Hist")
p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], color="purple", line_color="white")

# 2. Bar Plot (Direct grouping)
avg_bill = df.groupby('day')['total_bill'].mean()
p2 = figure(x_range=list(avg_bill.index), title="Avg Bill/Day")
p2.vbar(x=list(avg_bill.index), top=avg_bill, width=0.5, color="orange")

# 3. Scatter Plot (Directly passing column names/data)
p3 = figure(title="Bill vs Tip")
p3.scatter(df['total_bill'], df['tip'], size=8, color="green", alpha=0.6)

# Combine and Show
show(gridplot([[p1, p2], [p3]]))
