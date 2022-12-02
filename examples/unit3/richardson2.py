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
yy4 = [y]
yyex = [y]

for k in range(2):
    # Euler step.
    y1 = y + h * (lamb * y)

    # Two Euler half steps.
    hh = h * 0.5
    y2 = y
    for _ in range(2):
        y2 += hh * (lamb * y2)

    # Four Euler quarter steps.
    qh = h * 0.25
    y4 = y
    for _ in range(4):
        y4 += qh * (lamb * y4)

    # Richardson extrapolation (2-1) and (4-2)
    yr1 = y2 + (y2 - y1) / (2 - 1)
    yr2 = y4 + (y4 - y2) / (2 - 1)

    # Richardson extrapolation of Richardson extrapolations
    y = yr2 + (yr2 - yr1) / (2 ** 2 - 1)

    t += h

    tt.append(t)
    yy1.append(y1)
    yy2.append(y2)
    yy4.append(y4)
    yy.append(y)
    yexact = np.exp(lamb * t)
    yyex.append(yexact)

plt.figure(figsize=(4, 4))
plt.plot(tt, yy, marker='.', label='Richardson')
plt.plot(tt, yy4, marker='.', label='Euler h/4')
plt.plot(tt, yy2, marker='.', label='Euler h/2')
plt.plot(tt, yy1, marker='.', label='Euler h')
plt.plot(tt, yyex, label='exact', c='k')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.savefig('richardson2.pdf', bbox_inches='tight')
