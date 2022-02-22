import pandas

def load_iris():
    df = pandas.read_csv("iris.csv")
    df.columns = ["x1","x2","x3","x4"]
    df1 = pandas.read_csv('labels.csv')
    df['y']=df1.values
    return df
