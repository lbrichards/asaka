import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

plt.rcParams['font.size'] = 14

M = 2
k = 4
c = .5

nu = c / M
omega = k / M

def f(x_and_v, time, nu, omega):
    v = x_and_v[1]
    a = -nu * x_and_v[1] - omega * x_and_v[0]
    return np.array([v, a])

t = np.linspace(0, 100, 1000)
d_and_v = odeint(f, (1, .5), t, args=(nu, omega))


center = t.mean()

fig, ax = plt.subplots()
ax.grid()
ax.plot(t, d_and_v[:, 0], label=r'$d(t)$ [m]')
ax.plot(t, d_and_v[:, 1], label=r'$v(t)$ [m/s]')
ax.set_xlabel('$t$ [s]')
ax.legend()

spring = ax.plot([center] * 2, [0, d_and_v[0, 0]], 'k', lw=3)[0]
big_dot = ax.plot(center, d_and_v[0, 0], 'ko', ms=20)[0]
dot1 = ax.plot(t[0], d_and_v[0, 0], 'r*')[0]
dot2 = ax.plot(t[0], d_and_v[0, 1], 'g*')[0]

def animate(i):
    i = np.clip(int(round(i)), 0, len(t) - 1)
    tt = t[i]
    spring.set_data([center]*2, [0, d_and_v[i, 0]])
    big_dot.set_data([center, d_and_v[i, 0]])
    dot1.set_data([tt, d_and_v[i, 0]])
    dot2.set_data([tt, d_and_v[i, 1]])

    fig.canvas.draw_idle()

if 1:
    from matplotlib.widgets import Slider

    plt.subplots_adjust(bottom=0.2)

    axts = fig.add_axes([0.25, .03, 0.50, 0.02])
    ts = Slider(axts, 'step', 0, len(t) - 1, valinit=0, valfmt='%d')
    ts.on_changed(animate)

else:
    import matplotlib.animation as animation

    ani = animation.FuncAnimation(fig, animate, np.arange(len(t)),
                                  interval=(t[1] - t[0]) * 1000)

plt.show()