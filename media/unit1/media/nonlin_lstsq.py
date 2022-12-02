#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

np.random.seed(2022)

# Transmitter true location.
bx_t = 0.7
by_t = 0.37

# Beacon locations (randomly located in the unit square).
x_beac = np.array([
    0.7984, 0.9430, 0.6837, 0.1321, 0.7227, 0.1104, 0.1175, 0.6407, 0.3288,
    0.6538
])
y_beac = np.array([
    0.7491, 0.5832, 0.7400, 0.2348, 0.7350, 0.9706, 0.8669, 0.0862, 0.3664,
    0.3692
])

# Generate the (noisy) data y, and set initial guess.
y = np.empty(10)
dx = bx_t - x_beac
dy = by_t - y_beac
y = np.sqrt(dx**2 + dy**2)
noise_level = 0.05
y += np.random.rand(len(y)) * noise_level

b_init = np.array([0.4, 0.9])  # Initial guess.


# Objective function.
def phi(x):
    res = 0
    for i in range(len(x_beac)):
        dx = x[0] - x_beac[i]
        dy = x[1] - y_beac[i]
        ss = np.sqrt(dx**2 + dy**2) - y[i]
        res += ss * ss
    return res


# Gradietn objective function.
def grad_phi(x):
    f0 = 0
    f1 = 0
    for i in range(10):
        dx = x[0] - x_beac[i]
        dy = x[1] - y_beac[i]
        d = 1 / np.sqrt(dx**2 + dy**2)
        f0 += 2 * dx - 2 * y[i] * dx * d
        f1 += 2 * dy - 2 * y[i] * dy * d
    return np.array([f0, f1])


# Run Levenberg-Marquardt and print diagnostic information.
sol = root(grad_phi, b_init, jac=False, method='lm')
print("Predicted location:", sol.x)
print("grad(phi):", grad_phi(sol.x))
print("phi:", phi(sol.x))
print("phitrue:", phi([bx_t, by_t]))

# Plot results.
n = 100
xx = np.linspace(0, 1, n)
yy = np.linspace(0, 1, n)
X, Y = np.meshgrid(xx, yy)
pxy = phi([X, Y])

plt.figure(figsize=(2.5,2.5))
plt.scatter(x_beac, y_beac, marker='o', c='C0')  # Beacons.
plt.scatter(bx_t, by_t, marker='x', c='k', s=20)  # True transmitter.
plt.text(0.15, 0.8, "$x^i$")
plt.text(bx_t, by_t-0.1, "$\hat{b}$")
plt.gca().set_aspect('equal')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.savefig("nonlin_lstsq_1.svg")

plt.figure(figsize=(2.5,2.5))
plt.scatter(x_beac, y_beac, marker='o', c='C0')  # Beacons.
plt.scatter(bx_t, by_t, marker='x', c='k', s=20)  # True transmitter.
plt.scatter(sol.x[0], sol.x[1], marker='x', c='C4', s=20)  # Predicted transmitter.
plt.gca().set_aspect('equal')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.savefig("nonlin_lstsq_2.svg")

plt.figure(figsize=(2.5,2.5))
plt.contourf(X, Y, pxy, 16, alpha=.75)
plt.contour(X, Y, pxy, 16, colors='black', linewidths=0.5)
plt.scatter(x_beac, y_beac, marker='o', c='C0')  # Beacons.
plt.scatter(bx_t, by_t, marker='x', c='k', s=20)  # True transmitter.
plt.scatter(sol.x[0], sol.x[1], marker='x', c='C4', s=20)  # Predicted transmitter.
plt.gca().set_aspect('equal')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.savefig("nonlin_lstsq_3.svg")
