#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig

# Model constants.
lamb = 1.


# Function that evaluates the RHS of the ODE. It has two components,
# representing the changes in prey and predator populations.
def f(t, y):
    global lamb
    return [lamb * y]


def traj(y0, lamb):
    global t
    yinit = [y0]
    sol = scipy.integrate.solve_ivp(f,
                                    t_span=(t[0], t[-1]),
                                    y0=yinit,
                                    t_eval=t)
    return sol.y[0]


t = np.linspace(0, 1, 100)

y01 = 1.
y02 = 0.8

for lamb, suff, ylim in [
    (-1, 'm1', 3),
    (0, '0', 3),
    (1, '1', 3),
]:
    fig, ax = plt.subplots(figsize=(2.4, 1.6))
    y1 = traj(y01, lamb)
    y2 = traj(y02, lamb)
    ax.plot(t, y1, c='C0')
    ax.plot(t, y2, c='C1')
    ax.plot(t, abs(y1 - y2), c='C3')
    ax.set_xlabel('t')
    ax.set_ylabel('y')
    ax.set_ylim(0, ylim)
    ax.set_xticks([0, 0.5, 1])
    savefig(fig, suff='_' + suff)
    plt.close(fig)
