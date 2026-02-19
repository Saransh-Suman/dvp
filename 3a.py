# Write a Python program to Demonstrate how to Draw a Bar Plot using Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("./DataSet/Car_BarPlot.csv")
df = pd.DataFrame(data)

x = df.iloc[:,0]
y = df.iloc[:,1]

plt.bar(x,y,color = 'g')
plt.title("Car vs Sales bar Plot")
plt.xlabel("Car name")
plt.ylabel("Sales")
plt.show()