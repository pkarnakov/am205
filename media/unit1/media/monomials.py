#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt

def get_path(ext, suff=''):
    return os.path.splitext(os.path.basename(
        sys.argv[0]))[0] + suff + '.' + ext


def savefig(fig, suff=''):
    path = get_path('svg', suff)
    print(path)
    fig.savefig(path, metadata={'Date': None})


x = np.linspace(-1, 1, 500)

fig, ax = plt.subplots()
ax.set_ylim(-1.5, 1.5)
for i in range(6):
    lbl = 1 if i == 0 else 'x' if i == 1 else 'x^{{{:}}}'.format(i)
    ax.plot(x, x ** i, label=r"${}$".format(lbl))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(bbox_to_anchor=(1.1,0.9))
savefig(fig)
plt.close(fig)
