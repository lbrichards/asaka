import pandas

df = pandas.read_excel("430417.xlsx", skiprows=5, usecols=[0,1])
print(df.head())