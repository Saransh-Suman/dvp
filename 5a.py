import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,label = "Linear Funxtion: y = 2x")
plt.xlabel('X-Axis')
plt.ylabel("Y-Axis")
plt.title("Linear Plotting")
plt.legend()
plt.show()