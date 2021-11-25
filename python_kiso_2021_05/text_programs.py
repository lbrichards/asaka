from pprint import pprint


population = {
    "iwaki" : 350_237,
    "koriyama" : 335_444,
    "fukushima" : 294_247,
    "aizu-wakamatsu" : 131_389,
    "shirakawa" : 65_707
}

print(f"The population of Fukushima is {population['fukushima']}.")


k = "fukushima"
v = population["fukushima"]

print(f"The population of {k.capitalize()} is {v:,d}.")

population["fukushima"] = 294_000
print(f"The population of Fukushima is {population['fukushima']}.")
del population["fukushima"]
print(population)

population["nihonmatsu"] = 19_778

print(population)

pop2 = {
    "kitakata" : 16_755,
    "date" : 21_656
}

pop2.update(population)

pprint(pop2)

print(pop2.keys())

for k in pop2.keys():
    print(k)


for v in pop2.values():
    print(v)

for k, v in pop2.items():
    print(f"{k}の人口は{v:,d}です")

big_only = {k:v for k,v in pop2.items() if v>100_000}
print(big_only)


