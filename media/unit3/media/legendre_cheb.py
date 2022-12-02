#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import Legendre
from numpy.polynomial.chebyshev import Chebyshev
from util import get_path, savefig

x = np.linspace(-1, 1, 500)

fig, ax = plt.subplots()
ax.set_ylim(-1.5, 1.5)

n = 5

f = Chebyshev([0] * n + [1])
ax.plot(x, f(x), label=r"Chebyshev $T_{{{:}}}$".format(n))

f = Legendre([0] * n + [1])
ax.plot(x, f(x), label=r"Legendre $P_{{{:}}}$".format(n))

ax.axhline(y=0, ls='--', c='k', lw=0.5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(bbox_to_anchor=(1.1,0.9))
savefig(fig)
plt.close(fig)
