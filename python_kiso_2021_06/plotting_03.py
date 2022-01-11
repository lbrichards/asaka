from matplotlib import pyplot as plt
from numpy import load
import seaborn as sns
sns.set()
fish = load("fish.npy")
mean = fish.mean()
std = fish.std()
sns.displot(fish, kde=True, stat="density")
plt.axvline(mean, color='r')
plt.tight_layout()
plt.xlabel('kilograms')
plt.show()




