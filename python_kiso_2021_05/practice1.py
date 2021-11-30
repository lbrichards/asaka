from pprint import pprint

data = [
    {'female': 145090, 'male': 139783, 'name': '福島市'},
    {'female': 165891, 'male': 164180, 'name': '郡山市'},
    {'female': 169961, 'male': 166706, 'name': 'いわき市'}]

for d in data:
    d["total"] = d["male"] + d["female"]

pprint(data)