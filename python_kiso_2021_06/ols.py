from matplotlib import pyplot as plt
from numpy.linalg import inv
import numpy
import seaborn as sns
sns.set()

def f(x):
    c = numpy.array([4.2, -3.5, 4.6, -44.5, 54.3, 23])
    X = numpy.array([x**n for n in range(len(c))])
    return c @ X

x = numpy.linspace(-8, 8)
y = f(x) + 300 * numpy.random.normal(size=len(x), scale = 80, loc=0)

HIGHEST_POWER = 1
pows= [k for k in range(HIGHEST_POWER, -1, -1)]
A = numpy.vstack([x ** p for p in pows]).T

coeffs = inv(A.T @ A) @ A.T @ y

xn = numpy.linspace(-7,7)
X = numpy.array([xn**p for p in pows])
y_hat = X.T@coeffs
plt.plot(x, y, 'r.')
plt.plot(xn, y_hat, 'g.-')
plt.show()

