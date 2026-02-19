#Stack plot
import matplotlib.pyplot as plt
import numpy as np
days = np.arange(1,8)
apples = np.array([1,2,3,4,5,6,7])
bananas = np.array([2,4,6,8,10,12,14])
oranges = np.array([6,2,4,9,12,5,8])
fig,ans = plt.subplots(1,2,figsize = (12,5))
ans[0].stackplot(days,apples,bananas,oranges,labels = ['Apples','Bananas','Oranges'])
ans[0].set_title("Stackplot of days vs fruits")
ans[0].set_xlabel("Number of days")
ans[0].set_ylabel("Fruits")
ans[0].legend(loc = 'upper left')
ans[1].plot(days,apples,marker = 'o',color = 'blue')
ans[1].set_title("Days vs apples")
ans[1].set_xlabel("days")
ans[1].set_ylabel("Apples")
plt.show()