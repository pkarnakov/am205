#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt


def solve_wave(x, t, u_init, ut_init, rhs):
    """
    Solves the wave equation with zero Dirichlet conditions.
    """
    u = np.zeros((len(t), len(x)))
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    u[0] = u_init

    # First time step, second-order accurate.
    for i in range(1, len(x) - 1):
        u_xx = (u[0, i - 1] - 2 * u[0, i] + u[0, i + 1]) / dx**2
        u_tt = u_xx
        u[1] = u[0] + ut_init * dt + 0.5 * u_tt * dt**2

    # Further time steps.
    for n in range(1, len(t) - 1):
        # Bounary values remain unchanged.
        for i in range(1, len(x) - 1):
            u_xx = (u[n, i - 1] - 2 * u[n, i] + u[n, i + 1]) / dx**2
            u_tt = u_xx + rhs[n, i]
            u[n + 1, i] = 2 * u[n, i] - u[n - 1, i] + u_tt * dt**2
    return u


x = np.linspace(0, 1, 100)
dx = x[1] - x[0]
dt = dx * 0.25
tmax = 0.1
t = np.arange(0, tmax, dt)

# Zero initial derivatives and RHS.
ut_init = np.zeros_like(x)
rhs = np.zeros((len(t), len(x)))

# Initial value.
u_init = np.sin(2 * x * np.pi)

u = solve_wave(x, t, u_init, ut_init, rhs)

plt.figure(figsize=(4, 4))
for n in np.linspace(0, len(t) - 1, 3).astype(int):
    plt.plot(x, u[n], label="t={:.2f}".format(t[n]))
plt.xlabel('x')
plt.ylabel('u')
plt.legend(bbox_to_anchor=(1.4, 1.))
plt.savefig("wave.pdf", bbox_inches='tight')
