import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

sns.set()
b = 5
f = lambda x, y: (x - 1) ** 2 + b * (y - x ** 2) ** 2
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
plt.title("The Rosenbrock Function")

X = np.arange(-2, 2, 0.05)
Y = np.arange(-1, 3, 0.05)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.magma,
                       linewidth=0, antialiased=False)
ax.set_zlim(0, 130)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
divider = make_axes_locatable(ax)
fig.colorbar(surf)
plt.show()
