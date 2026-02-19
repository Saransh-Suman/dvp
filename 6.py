# Write a Python program which explains uses of customizing seaborn plots with Aesthetic functions
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.scatterplot(data = tips, x= 'total_bill',y = 'tip',size = 'size')
sns.despine()
plt.xlabel('Total bill')
plt.ylabel('Tips')
plt.title("Total bill vs tips scatterplot")
plt.show()
