import pandas

df = pandas.read_csv("iris.csv")
print(df.shape)
print(df.describe())
df.columns = ["x1","x2","x3","x4"]
print(df.head())
print(df.tail())

df1 = pandas.read_csv('labels.csv')
df['y']=df1.values

print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

df["id"] = df.index
df["ratio"] = df.x1/df.x2
species = df.y

sns.lmplot(x="id", y="ratio", data=df, hue="y", fit_reg=False, legend=False)

plt.legend()
plt.show()

