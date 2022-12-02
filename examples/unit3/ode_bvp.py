#!/usr/bin/env python3

import numpy as np
from numpy import pi, cos, sin, exp
import matplotlib.pyplot as plt

# ODE parameters.
alpha = 0.5
beta = -2.0
gamma = 0.1

# Length of interval and boundary conditions.
c_1 = 0.0
c_2 = 0.0
a = 0.0
b = 1.0

# Set grid resolution.
n = 11
x = np.linspace(a, b, n)
h = x[1] - x[0]

# Generate the centered difference differentiation matrix for u'.
f = 1.0 / (2 * h)
D1 = np.diag(-np.ones(n - 1) * f, -1) + np.diag(np.ones(n - 1) * f, 1)

# Generate the centered difference differentiation matrix for u''.
f = 1 / (h * h)
D2 = np.diag(-np.ones(n) * f * 2) + np.diag(np.ones(n - 1) * f, 1) + np.diag(
    np.ones(n - 1) * f, -1)

# Build the system matrix A.
A = -alpha * D2 + beta * D1 + gamma * np.identity(n)

# Define the right-hand side vector.
F = (-alpha * exp(x) * (4 * pi * cos(2 * pi * x) +
                        (1 - 4 * pi * pi) * sin(2 * pi * x)) + beta * exp(x) *
     (sin(2 * pi * x) + 2 * pi * cos(2 * pi * x)) +
     gamma * exp(x) * sin(2 * pi * x))

# Set first and last rows of A to enforce Dirichlet conditions.
A[0, 0] = 1
A[0, 1] = 0
A[n - 1, n - 2] = 0
A[n - 1, n - 1] = 1

# Set first and last rows of F.
F[0] = c_1
F[n - 1] = c_2

# Solve the linear system.
U = np.linalg.solve(A, F)

# Exact solution.
Uex = exp(x) * sin(2 * pi * x)

# Plot.
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(4, 7))
ax.plot(x, U, label='approx')
ax.plot(x, Uex, label='exact')
ax1.plot(x, U - Uex, label='error')
ax1.set_xlabel('x')
ax.set_ylabel('u')
ax1.set_ylabel('error')
ax.legend()
fig.savefig('ode_bvp.pdf', bbox_inches='tight')
