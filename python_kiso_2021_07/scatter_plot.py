from matplotlib import pyplot as plt
from prepare_data import load_iris

df = load_iris()

plt.figure(figsize=(5, 4))

plt.scatter(df.x1, df.x2, c=df.y)
plt.grid()
plt.tight_layout()
plt.show()