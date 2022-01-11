
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator
from numpy import linspace, sin, pi
import matplotlib.font_manager as fm
props = fm.FontProperties()
props.set_name('Hiragino Sans')
props.set_size('x-large')
plt.rc('legend',fontsize=20)
TWOPI = 2*pi
t = linspace(-TWOPI,TWOPI,50)
y = sin(t)
plt.style.use("ggplot")
fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(111)
plt.plot(t, y, 'r', label="y=sin(t)", alpha=.2, lw=5)

plt.title("正弦波", fontdict={'fontproperties':props})
plt.grid(True)
plt.ylim(-1.3, 1.3)
# plt.axis("equal")
plt.legend(loc="best")
ax1.xaxis.set_major_formatter(
   FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/pi) if val !=0 else '0'
))
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.xaxis.set_major_locator(MultipleLocator(base=pi))
# plt.show()
plt.savefig('sin2.pdf')