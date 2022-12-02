#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

c = 1  # Advection speed.
nx = 128  # Grid size in space.
x = np.linspace(0, 1, nx, endpoint=False)  # Grid in space.
dx = x[1] - x[0]  # Step in space.

nu = 0.1  # CFL number.

tmax = 0.1  # Time range.
dt = dx * nu / c  # Step in time.

t = np.arange(0, tmax + 0.1 * dt, dt)  # Grid in time.
nt = len(t)

# Initial condition.
u_init = np.exp(-20 * (x - 0.5)**2)
#u_init = np.sign(x - 0.5)


def upwind():
    u = np.zeros((nt, nx))  # Solution.

    u[0] = u_init
    for n in range(nt - 1):
        for i in range(0, nx):
            im = i - 1 if i > 0 else nx - 1
            ip = i + 1 if i < nx - 1 else 0
            u[n + 1, i] = (1 - nu) * u[n, i] + nu * u[n, im]
    return u


def central():
    u = np.zeros((nt, nx))  # Solution.

    u[0] = u_init
    for n in range(nt - 1):
        for i in range(0, nx):
            im = i - 1 if i > 0 else nx - 1
            ip = i + 1 if i < nx - 1 else 0
            u[n + 1, i] = u[n, i] + 0.5 * nu * (u[n, im] - u[n, ip])
    return u



u = upwind()
#u = central()

plt.figure(figsize=(4, 4))
for n in np.linspace(0, nt - 1, 3).astype(int):
    plt.plot(x, u[n], label="t={:.2f}".format(t[n]))
plt.xlabel('x')
plt.ylabel('u')
plt.legend(bbox_to_anchor=(1.4, 1.))
plt.savefig("advection.pdf", bbox_inches='tight')
