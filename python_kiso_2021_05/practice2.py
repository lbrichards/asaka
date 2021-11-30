import json
from pprint import pprint

fname = "periodic_table.json"

with open(fname, "r") as f:
    data = json.load(f) # loadは「荷を積む」という意味

print(data.keys())

def by_atomic_mass(d):
    return d["atomic_mass"]



#print(len(data["elements"]))
for e in sorted(data["elements"], key=by_atomic_mass):

    pprint(e["atomic_mass"])
#     print(f"""
# {e['symbol']} is the symbol for {e['name']}.
# It boils at {e['boil']} K and melts at {e['melt']} K.
# """)

