#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import Legendre
from util import get_path, savefig

x = np.linspace(-1, 1, 500)

fig, ax = plt.subplots()
ax.set_ylim(-1.5, 1.5)
for i in range(6):
    f = Legendre([0] * i + [1])
    ax.plot(x, f(x), label=r"$P_{{{:}}}$".format(i))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(bbox_to_anchor=(1.1,0.9))
savefig(fig)
plt.close(fig)
