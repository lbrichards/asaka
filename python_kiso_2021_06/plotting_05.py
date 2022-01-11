from matplotlib import pyplot as plt
from numpy import sin, cos, linspace, meshgrid

def f(x, y):
    return sin(x) ** 10 + cos(10 + y * x)

x = linspace(0, 5, 1000)
y = linspace(0, 5, 1000)

X, Y = meshgrid(x, y)
Z = f(X, Y)


plt.title("Plot of complex 2d function")
plt.imshow(Z, cmap="viridis")
plt.colorbar()
plt.show()
