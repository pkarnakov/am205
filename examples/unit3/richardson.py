#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Initial variables and constants.
y = 1
t = 0
h = 0.5
lamb = 2

# Equation `dy/dt = lamb * y`

tt = [t]
yy = [y]
yy1 = [y]
yy2 = [y]
yyex = [y]

for k in range(2):
    # Euler step.
    y1 = y + h * (lamb * y)

    # Two Euler half steps.
    hh = h * 0.5
    yh = y + hh * (lamb * y)
    y2 = yh + hh * (lamb * yh)

    # Richardson extrapolation.
    y = y2 + (y2 - y1) / (2 - 1)

    t += h

    tt.append(t)
    yy1.append(y1)
    yy2.append(y2)
    yy.append(y)
    yexact = np.exp(lamb * t)
    yyex.append(yexact)


plt.figure(figsize=(4,4))
plt.plot(tt, yy, marker='.', label='Richardson')
plt.plot(tt, yy2, marker='.', label='Euler h/2')
plt.plot(tt, yy1, marker='.', label='Euler h')
plt.plot(tt, yyex, label='exact', c='k')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.savefig('richardson.pdf', bbox_inches='tight')
