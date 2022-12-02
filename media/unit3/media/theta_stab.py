#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

x1 = np.linspace(0, 1, 500)
y1 = np.linspace(0, 12, 500)

x, y = np.meshgrid(x1, y1)

fig, ax = plt.subplots()
f = y - 1 / (2 * (1 - 2 * x))
f *= np.sign(0.5 - x)
ax.contourf(x1, y1, f, levels=[-1e5, 0], colors=['C1'])
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\mu$')
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_ylim(0, 12)
ax.axvline(x=0.5, c='k', ls='--')
savefig(fig)
plt.close(fig)
