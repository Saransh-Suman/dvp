# Write a Python program to Demonstrate how to draw a Scatter Plot using Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("./DataSet/cars.csv")
x = data['Age']
y = data['Price']

plt.scatter(x,y,color = 'blue')
plt.title("Age vs Price scatter plot")
plt.xlabel("Age")
plt.ylabel("Price")
plt.show()