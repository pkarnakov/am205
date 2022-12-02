#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from util import get_path, savefig

plt.rcParams.update({
    "axes.spines.right": True,
    "axes.spines.top": True,
})

n = 11
h = 1 / (n - 1)
D = np.diag(-np.ones(n) / h) + np.diag(np.ones(n - 1) / h, 1)
fig, ax = plt.subplots()
ax.spy(D, marker='s', markersize=7)
savefig(fig)
plt.close(fig)


fig, ax = plt.subplots()
D[-1, -1] = 1 / h
D[-1, -2] = -1 / h
ax.spy(D, marker='s', markersize=7)
savefig(fig, suff='_bc')
plt.close(fig)
