#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig


x = np.linspace(-2, 10, 500)

fig, ax = plt.subplots(figsize=(4,2))
ax.set_ylim(-0.2, 1.2)
for t in np.linspace(0, 6, 4):
    ax.plot(x, np.exp(-(1 - (x - t)) ** 2), label=r'$t={:.0f}$'.format(t))

ax.set_xlabel('x')
ax.set_ylabel('u')
ax.legend(bbox_to_anchor=(1.2,0.9))
savefig(fig)
plt.close(fig)
