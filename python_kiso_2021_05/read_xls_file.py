import json
from copy import deepcopy
from dataclasses import dataclass
from pprint import pprint

import pandas

from path import Path
cwd = Path("/Users/macmini/projects/asaka/asaka/python_kiso_2021_05")
cwd.chdir()

print(cwd)

@dataclass
class Datum:
    name : str
    total : int
    male : int
    female : int

    def as_dict(self):
        return {
            "name":self.name,
            "total": self.total,
            "male" : self.male[1],
            "female" : self.female[1]
        }

    def as_dict_no_total(self):
        return {
            "name": self.name,
            "male": self.male[1],
            "female": self.female[1]
        }

NullDatum = Datum(None, None, None, None)

def datum_from_df(df):
    try:
        assert len(df) == 3
        assert not df.isnull().values.any()
    except AssertionError:
        raise(Exception())
    df.index = range(len(df))
    name = df.k[0]
    total = df.v[0]
    male = df[df.k == 'うち男'].values[0]
    female = df[df.k == 'うち女'].values[0]
    try:
        df.v = df.v.astype(int)
    except:
        return NullDatum
    return Datum(name, total, male, female)



def get_data():
    df = pandas.read_excel("430417.xlsx", skiprows=5, usecols=[0,1])
    df = df.rename(columns = {"Unnamed: 0":"k", "Unnamed: 1":"v"})
    return df

def repair_data(df):
    x = '\u3000'
    def f(s):
        while x in s:
            s = s.strip(x)
        return s
    df.k = deepcopy(df.k.apply(lambda s: f(s)))
    return df

def has_dash(df):
    condition1 =  "-" in df.v
    condition2 = any([type(val) is not int for val in df.v])

    if condition1:
        return True
    if condition2:
        return True
    try:
        condition3 = any([int(val) < 0 for val in df.v])
    except:
        return True
    return condition3

df = get_data()
df = repair_data(df)

data = []
for i, row in df.iterrows():
    if 'うち女' in row.k:
        df2 = df[i-2:i+1]
        df3 = deepcopy(df2)
        if not has_dash(df3):
            data.append(
                datum_from_df(df3))
        del df2

data = [d.as_dict_no_total() for d in data if d is not NullDatum]

with open("population.json", "w") as f:
    json.dump(data, f)

# print([d.as_dict() for d in data])

with open("population.json", "r") as f:
    data2 = json.load(f)

def big_enough(d):
    return d["male"] + d["female"] > 250_000


out = [e for e in data if big_enough(e)]
# data3 = {k:v for k,v in (e.items() for e in data2) if v>400000}
pprint(out)
