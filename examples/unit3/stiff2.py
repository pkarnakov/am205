#!/usr/bin/env python3
from scipy.integrate import ode
from math import exp
import matplotlib.pyplot as plt


# Function
def f(t, y, arg1):
    return [998 * y[0] + 1998 * y[1], -999 * y[0] - 1999 * y[1]]


# Initial conditions
yinit = [1, 0]

# Set up stiff integrator and parameters
r = ode(f).set_integrator('zvode', method='bdf')
r.set_initial_value(yinit, 0).set_f_params(2.0).set_jac_params(2.0)
h = 0.05

vt = []
vex1 = []
vex2 = []
vy1 = []
vy2 = []
ve1 = []
ve2 = []

# Loop while the time is less than 2
while r.successful() and r.t < 2:
    r.integrate(r.t + h)

    # Print solution and comparison with exact answer
    ex1 = 2 * exp(-r.t) - exp(-1000 * r.t)
    ex2 = -exp(-r.t) + exp(-1000 * r.t)

    vt.append(r.t)
    vex1.append(ex1)
    vex2.append(ex2)
    vy1.append(float(r.y[0]))
    vy2.append(float(r.y[1]))
    ve1.append(float(r.y[0]) - ex1)
    ve2.append(float(r.y[1]) - ex2)

plt.figure(figsize=(4,4))
plt.plot(vt, vex1)
plt.plot(vt, vy1)
plt.xlabel('t')
plt.savefig('stiff2.pdf', bbox_inches='tight')
