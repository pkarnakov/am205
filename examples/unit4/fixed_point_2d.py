#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# Function.
def f(x1, x2):
    return (x1 * x1 + x2 * x2 - 1, 5 * x1 * x1 + 21 * x2 * x2 - 9)


fig, ax = plt.subplots()

# Starting position.
(x1, x2) = (0., 0.)

ax.scatter(x1, x2, c='b', zorder=5, label='start')

# Fixed-point iteration
for k in range(15):
    x1p = np.sqrt(1 - x2 * x2)
    x2p = np.sqrt((9. - 5. * x1 * x1) / 21.)
    print(
        "x=({:8.5f}, {:8.5f})".format(x1, x2),
        "  f(x)=({:8.5f}, {:8.5f})".format(*f(x1, x2)),
        "  |f(xp)|/|f(x)|={:8.5f}".format(
            np.linalg.norm(f(x1p, x2p)) / np.linalg.norm(f(x1, x2))),
    )
    ax.plot([x1, x1p], [x2, x2p], c='k', zorder=5, marker='.')
    x1, x2 = x1p, x2p

ax.scatter(x1, x2, c='r', zorder=5, label='final')
ax.legend()

ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
fig.savefig("fixed_point_2d.pdf")
