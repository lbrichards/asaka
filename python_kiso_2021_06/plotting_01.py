from matplotlib import pyplot as plt
from numpy import linspace, sin, pi
TWOPI = 2*pi
t = linspace(-TWOPI, TWOPI, 50)
y = sin(t)
plt.plot(t,y)
# plt.show()
plt.savefig('sin1.pdf')