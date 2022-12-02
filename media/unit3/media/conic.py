#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

x1 = np.linspace(-4, 4, 500)
y1 = np.linspace(-4, 4, 500)

x, y = np.meshgrid(x1, y1)

p = 'hyper'
fig, ax = plt.subplots(figsize=(1.7,1.7))
f = y ** 2 - x ** 2
ax.contour(x1, y1, f, levels=[0., 2., 4., 6.], colors=['C0', 'C1', 'C2', 'C3' ])
ax.set_xlabel('$x$')
ax.set_ylabel('$t$')
ax.set_aspect('equal')
ax.set_xticks([-4, -2, 0, 2, 4])
ax.set_yticks([-4, -2, 0, 2, 4])
suff = "_{:}".format(p)
savefig(fig, suff=suff)
plt.close(fig)

p = 'ell'
fig, ax = plt.subplots(figsize=(1.7,1.7))
f = x ** 2 + y ** 2
ax.contour(x1, y1, f, levels=[0., 2., 4., 6.], colors=['C0', 'C1', 'C2', 'C3' ])
ax.scatter([0], [0], marker='.', s=3, c='C0')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_aspect('equal')
ax.set_xticks([-4, -2, 0, 2, 4])
ax.set_yticks([-4, -2, 0, 2, 4])
suff = "_{:}".format(p)
savefig(fig, suff=suff)
plt.close(fig)


p = 'para'
x1 = np.linspace(-5, 5, 500)
y1 = np.linspace(0, 16, 500)
x, y = np.meshgrid(x1, y1)
fig, ax = plt.subplots(figsize=(1.7,1.7))
f = y - x ** 2
ax.contour(x1, y1, f, levels=[0., 2., 4., 6.], colors=['C0', 'C1', 'C2', 'C3' ])
ax.set_xlabel('$x$')
ax.set_ylabel('$t$')
suff = "_{:}".format(p)
savefig(fig, suff=suff)
plt.close(fig)
