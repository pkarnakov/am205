#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# RHS of differential equation to integrate
lamb = 0.5
tend = 2.


def f(y):
    return lamb * y

def exact(t):
    return np.exp(lamb * t)

# Function to perform Adams-Bashforth integration over the range 0<=t<=2, and
# evaluate error
def adams(n):
    h = tend / n

    # Initialize two values to exactly match solution.
    y = [exact(0), exact(h)]

    # Perform Adams-Bashforth updates.
    for i in range(n - 1):
        yy = y[1] + h * (1.5 * f(y[1]) - 0.5 * f(y[0]))
        y[0] = y[1]
        y[1] = yy

    # Return error between numerical result and exact solution.
    return abs(y[1] - exact(tend))


# Evaluate error for different numbers of timesteps.
n = 2
nn = []
hh = []
err = []
while n <= 65536:
    nn.append(n)
    hh.append(tend / n)
    err.append(adams(n))
    n *= 2

plt.figure(figsize=(4,4))
plt.plot(hh, err, marker='.')
plt.plot(hh, np.array(hh) ** 2, marker='.')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('error')
plt.savefig('adams.pdf', bbox_inches='tight')
