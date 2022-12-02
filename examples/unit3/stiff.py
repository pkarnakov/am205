#!/usr/bin/env python3

import numpy as np
from math import exp
import matplotlib.pyplot as plt

# Matrices
a = np.array([[998, 1998], [-999, -1999]])
i = np.identity(2)

# Initial conditions
ye = np.array([[1], [0]])
yi = np.array([[1], [0]])

# Starting time and timestep (currently chosen within the stability region of
# the explicit method)
t = 0
h = 0.0001

vt = []
vex1 = []
vex2 = []
vye1 = []
vye2 = []
vyi1 = []
vyi2 = []


while t < 2:
    # Print solutions and exact solution
    ex1 = 2 * exp(-t) - exp(-1000 * t)
    ex2 = -exp(-t) + exp(-1000 * t)
    vt.append(t)
    vex1.append(ex1)
    vex2.append(ex2)
    vye1.append(ye[0, 0])
    vye2.append(ye[1, 0])
    vyi1.append(yi[0, 0])
    vyi2.append(yi[1, 0])

    # Explicit step
    ye = ye + h * np.dot(a, ye)

    # Implicit step
    yi = np.linalg.solve(i - h * a, yi)
    t += h

plt.figure(figsize=(4,4))
plt.plot(vt, vex1)
plt.plot(vt, vyi1)
plt.plot(vt, vye1)
plt.xlabel('t')
plt.savefig('stiff.pdf', bbox_inches='tight')
