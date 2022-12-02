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
def f(y, t):
    return [
        alpha1 * y[0] - beta1 * y[0] * y[1],
        -alpha2 * y[1] + beta2 * y[0] * y[1],
    ]


# Time points of interest.
t = np.linspace(0, 70, 500)

# Initial conditions, populations of prey and predators.
yinit = [10, 5]

# Solve the problem, the result will have shape `(len(t), 2)`.
y = scipy.integrate.odeint(f, yinit, t)

# Plot the solution.
plt.figure()
plt.plot(t, y[:, 0], label='prey', c='g')
plt.plot(t, y[:, 1], label='predator', c='r')
plt.legend()
plt.xlabel('t')
plt.ylabel('population')
plt.savefig('lotka_volterra.pdf')
