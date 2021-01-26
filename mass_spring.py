import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

plt.rcParams['font.size'] = 14

M = 5
k = 4
c = .5

ν = c / M
ω = k / M

def f(u, t, ν, ω):
    """
    u: [x,v]
    δu/δt = f(u) = [δx/δt, δv/δt] = [v, a]

    1) Ma + kv + cx = 0
    2) Ma = -kv - cx
    3) let ν = c/M; ω=k/m
    4) a = -νv - ωx
    5) δv/δt = -νv - ωx = u[1]
    6) by definition, v = δx/δt = u[0]
    ∴ δu/δt = f(u) = f(x,v) = [δx/δt, δv/δt] = [v, a]
    """
    v = u[1]
    a = -ν  * u[1] - ω * u[0]
    return np.array([v, a])

t = np.linspace(0, 100, 1000)
u = odeint(f, (1, .5), t, args=(ν, ω))

center = t.mean()

fig, ax = plt.subplots()
ax.grid()
ax.plot(t, u[:, 0], label=r'$x(t)$ [m]')
ax.plot(t, u[:, 1], label=r'$v(t)$ [m/s]')
ax.set_xlabel('$t$ [s]')
ax.legend()

spring = ax.plot([center] * 2, [0, u[0, 0]], 'k', lw=3)[0]
big_dot = ax.plot(center, u[0, 0], 'ko', ms=20)[0]
dot1 = ax.plot(t[0], u[0, 0], 'r*')[0]
dot2 = ax.plot(t[0], u[0, 1], 'g*')[0]

def animate(i):
    i = np.clip(int(round(i)), 0, len(t) - 1)
    tt = t[i]
    spring.set_data([center]*2, [0, u[i, 0]])
    big_dot.set_data([center, u[i, 0]])
    dot1.set_data([tt, u[i, 0]])
    dot2.set_data([tt, u[i, 1]])

    fig.canvas.draw_idle()

if 0:
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