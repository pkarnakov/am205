#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

alpha = 1  # Difusivity.
nx = 64  # Grid size in space.
x = np.linspace(0, 1, nx)  # Grid in space.
dx = x[1] - x[0]  # Step in space.

mu = 0.5  # Diffusion number.

tmax = 0.01  # Time range.
dt = dx ** 2 * mu / alpha  # Step in time.

t = np.arange(0, tmax + 0.1 * dt, dt)  # Grid in time.
nt = len(t)

# Initial condition.
#u_init = np.exp(-20 * (x - 0.5)**2)
u_init = np.where((x > 0.25) & (x < 0.75), 1., 0.)


def euler():
    u = np.zeros((nt, nx))  # Solution.
    u[0] = u_init
    for n in range(nt - 1):
        for i in range(1, nx - 1):
            im = i - 1 if i > 0 else nx - 1
            ip = i + 1 if i < nx - 1 else 0
            u[n + 1, i] = ((1 - 2 * mu) * u[n, i] + mu * (u[n, im] + u[n, ip]))
    return u


def crank_nicolson():
    u = np.zeros((nt, nx))  # Solution.
    u[0] = u_init

    # Create linear system matrix for implicit step in Crank-Nicolson.
    # Note that here the system is solved  using a dense solver,
    # which is inefficient. In practice, use a sparse linear solver.
    A = np.diag(np.ones(nx) * (1 + mu)) \
            + np.diag(np.ones(nx - 1) * (-0.5 * mu), 1) \
            + np.diag(np.ones(nx - 1) * (-0.5 * mu), -1)
    rhs = np.zeros(nx)
    # Boundary conditions.
    A[0, 0] = 1
    A[0, 1] = 0
    A[nx - 1, nx - 1] = 1
    A[nx - 1, nx - 2] = 0
    # Perform timesteps.
    for n in range(nt - 1):
        for i in range(1, nx - 1):
            im = i - 1 if i > 0 else nx - 1
            ip = i + 1 if i < nx - 1 else 0
            rhs[i] = (1 - mu) * u[n, i] + 0.5 * mu * (u[n, im] + u[n, ip])
        u[n + 1] = np.linalg.solve(A, rhs)
    return u


#u = euler()
u = crank_nicolson()

plt.figure(figsize=(4, 4))
for n in np.linspace(0, nt - 1, 3).astype(int):
    plt.plot(x, u[n], label="t={:.3f}".format(t[n]))
plt.xlabel('x')
plt.ylabel('u')
plt.legend(bbox_to_anchor=(1.4, 1.))
plt.savefig("heat.pdf", bbox_inches='tight')
