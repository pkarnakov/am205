#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2022)

N = 100
x = np.random.normal(size=N) * 0.35
y = np.random.normal(size=N) * 0.35
x += y * 1.5
x += 0.1
y += 0.3

xbar = x.mean()
ybar = y.mean()

plt.figure(figsize=(3, 3))
plt.gca().set_aspect('equal')
plt.scatter(x, y, c='k', s=1)
plt.scatter(xbar, ybar)

A = np.array([x - xbar, y - ybar]).T
(U, S, VT) = np.linalg.svd(A)
V = VT.T

v0 = V[:, 0]
v1 = V[:, 1]

plt.arrow(xbar, ybar, v0[0], v0[1], color='r')
plt.arrow(xbar, ybar, v1[0], v1[1], color='b')
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.savefig('pca.pdf', bbox_inches='tight')
