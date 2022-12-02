#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig

alpha = 1
beta = 0
gamma = -5

# Second-order equation: -alpha * uxx + beta * ux  + gamma * u= 0
#                         or  uxx = (beta * ux + gamma * u) / alpha
# Reduced to a system with unknowns v = (u, ux)
# Returns the RHS: v' = f(v, x)
def f(v, x):
    u, ux = v
    return [
        ux,
        (beta * ux + gamma * u) / alpha,
    ]

def ivp(u0, ux0):
    u = scipy.integrate.odeint(f, [u0, ux0], x)[:, 0]
    return u

x = np.linspace(0, 1, 500)

# Dirichlet conditions
# u(0) = c1
# u(1) = c2
c1 = 0
c2 = 0.5

# Neumann condition
# u'(0) = g

fig, ax = plt.subplots()

ax.scatter(1, c2, c='k')

# Iterate over various `g`.
for g in np.linspace(-1, 1, 11):
    u = ivp(c1, g)
    #ax.plot(x, u, c='C0')

g = 0
eta = 2
for s in range(4):
    u = ivp(c1, g)
    ax.plot(x, u, label=r"$g={:.3g}$".format(g))
    g += (c2 - u[-1]) * eta

ax.set_xlim(0, 1.1)
ax.set_ylim(-0.1, 1)
ax.set_xlabel('x')
ax.set_ylabel('u')
ax.legend()
savefig(fig)
plt.close(fig)
