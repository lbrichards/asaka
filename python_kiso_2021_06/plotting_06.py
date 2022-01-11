from matplotlib import pyplot as plt
import seaborn as sns
import numpy
sns.set()

b = 5
f = lambda x, y: (x - 1) ** 2 + b * (y - x ** 2) ** 2
x = numpy.linspace(-1, 1, 1000)
y = numpy.linspace(-1, 1, 1000)

X, Y = numpy.meshgrid(x, y)
Z = f(X, Y)

plt.title("The Rosenbrock Function (2)")
cont = plt.contour(X, Y, Z, 50, cmap='magma')
plt.colorbar(cont)
plt.show()
