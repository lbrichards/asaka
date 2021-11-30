from pprint import pprint

from fukushima_population import data



import json
with open('periodic_table.json', 'r') as f:
    t = json.load(f)

# print(t)

for i in range(len(t["elements"])):
    n = t["elements"][i]["name"]
    sym = t["elements"][i]["symbol"]
    print(f"{n}という元素は{sym}と表記する")

# lookup = {}
# for e in t["elements"]:
#     lookup[e["symbol"]]=e["name"]
#
# lookup = {}

lookup = {e["symbol"]:e["name"] for e in t["elements"]}


symbol = "Cu"
print(f"{symbol} is the symbol for {lookup[symbol]}")