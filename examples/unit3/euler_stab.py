#!/usr/bin/env python3

from math import exp
import matplotlib.pyplot as plt

# Initial variables and constants
y = 1
t = 0
h = 0.1

# Equation: dy/dt = lamb*y.
# Forward Euler is stable for `-2 <= h*lamb <= 0`.
lamb = -21
print('h * lamb =', h * lamb)

tt = [t]
yy = [y]
yyex = [y]
# Apply forward Euler step until t>1
while t <= 1:
    yexact = exp(lamb * t)
    y = y + h * (lamb * y)
    t += h
    tt.append(t)
    yy.append(y)
    yyex.append(yexact)

plt.plot(tt, yy)
plt.plot(tt, yyex)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('euler_stab.pdf')
