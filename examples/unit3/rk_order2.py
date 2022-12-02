#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Model parameters.
alpha1 = 1.2
beta1 = 0.4
alpha2 = 0.2
beta2 = 0.1


# Function that evaluates the RHS of the ODE. It has two components,
# representing the changes in prey and predator populations.
def f(t, y):
    return np.array([
        alpha1 * y[0] - beta1 * y[0] * y[1],
        -alpha2 * y[1] + beta2 * y[0] * y[1],
    ])


def euler(f, t, y, h):
    y = y + h * f(t, y)
    return y


def rk2_midpoint(f, t, y, h):
    y = y + h * f(t + 0.5 * h, y + 0.5 * h * f(t, y))
    return y


def rk2_heun(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    y = y + 0.5 * h * (k1 + k2)
    return y


def rk2_ralston(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + 2 * h / 3, y + 2 * h / 3 * k1)
    y = y + 0.25 * h * (k1 + 3 * k2)
    return y


# Time points of interest.
t = np.linspace(0, 20, 300)

# Initial conditions, populations of prey and predators.
yinit = [10, 5]

fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(5, 8))

# Scipy.
sol = scipy.integrate.solve_ivp(f,
                                t_span=(t[0], t[-1]),
                                y0=yinit,
                                t_eval=t,
                                rtol=1e-9)
yref = sol.y[0]
ax0.plot(t, yref, label='scipy', c='k')

for method, lbl in [
    (euler, 'euler'),
    (rk2_midpoint, 'midpoint'),
    (rk2_heun, 'heun'),
    (rk2_ralston, 'ralston'),
]:
    y = np.zeros((len(t), 2))
    y[0] = yinit
    for k in range(len(t) - 1):
        y[k + 1] = method(f, t[k], y[k], t[k + 1] - t[k])
    l, = ax0.plot(t, y[:, 0], label=lbl)
    ax1.plot(t, abs(y[:, 0] - yref), c=l.get_color())

fig.legend(bbox_to_anchor=(1.2, 0.8))
ax0.set_xlabel('t')
ax0.set_ylabel('prey population')
ax1.set_ylabel('error')
ax1.set_yscale('log')
fig.savefig('rk_order2.pdf', bbox_inches='tight')
