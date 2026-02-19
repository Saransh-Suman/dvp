# Write a Python program to Demonstrate how to draw a Histogram using Matplotlib
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("./DataSet/cars.csv")
plt.hist(data['KM'],bins = 5, color = "green",edgecolor = 'white')
plt.title("Histogram")
plt.xlabel("Kilometers")
plt.ylabel("Frequency")
plt.show()