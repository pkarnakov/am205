#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

x = np.array(range(11))
y = (-1) ** x

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel(r'$j$')
ax.set_ylabel(r'$e^{\pi i j}$')
ax.scatter(x, 0 * x, c='k', clip_on=False)
ax.set_ylim(-1.5, 1.5)
savefig(fig)
plt.close(fig)
