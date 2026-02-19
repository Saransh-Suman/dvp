# Write a Python program to Demonstrate how to draw a Piechart using Matplotlib
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("./DataSet/Car_BarPlot.csv")
plt.pie(data['Sales'],labels = data['Car'])
plt.show()