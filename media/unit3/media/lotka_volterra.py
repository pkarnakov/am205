#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig

# Model constants.
alpha1 = 1.2
beta1 = 0.4
alpha2 = 0.2
beta2 = 0.1


# Function that evaluates the RHS of the ODE. It has two components,
# representing the changes in prey and predator populations.
def f(t, y):
    return [
        alpha1 * y[0] - beta1 * y[0] * y[1],
        -alpha2 * y[1] + beta2 * y[0] * y[1],
    ]


# Time points of interest.
time = np.linspace(0, 70, 500)

# Initial conditions, populations of prey and predators.
yinit = [10, 5]

# Solve the problem, the result will have shape `(len(time), 2)`.
sol = scipy.integrate.solve_ivp(f,
                                t_span=(time[0], time[-1]),
                                y0=yinit,
                                t_eval=time)

# Plot the solution.
fig, ax = plt.subplots(figsize=(4, 1.5))
p0, = ax.plot(time, sol.y[0], label='prey', c='C1')
p1, = ax.plot(time, sol.y[1], label='predator', c='C0')
ax.set_xlabel('t')
ax.set_ylabel('population')
ax.legend(ncol=2, bbox_to_anchor=(0.3, 1.))
savefig(fig)
plt.close(fig)
