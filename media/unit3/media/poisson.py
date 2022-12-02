#!/usr/bin/env python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.sparse

# Grid size.
nx = 6
ny = nx
nxy = nx * ny

x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
h = x[1] - x[0]


def rhs_func(x, y):
    return -10


# Mapping from (i,j) to flat index.
def G(i, j):
    return j * nx + i


# Create a sparse differentiation matrix.

data = []  # Elements.
rows = []  # Row indices, correspond to equations.
cols = []  # Column indices, correspond to unknowns.
rhs = np.zeros(nxy)  # Right-hand side.
hfac = 1 / (h * h)

for i in range(nx):
    for j in range(nx):
        if i > 0 and i < nx - 1 and j > 0 and j < ny - 1:
            # Inner node, append equation approximation.
            data.append(-4 * hfac)
            rows.append(G(i, j))
            cols.append(G(i, j))

            data.append(hfac)
            rows.append(G(i, j))
            cols.append(G(i - 1, j))

            data.append(hfac)
            rows.append(G(i, j))
            cols.append(G(i + 1, j))

            data.append(hfac)
            rows.append(G(i, j))
            cols.append(G(i, j - 1))

            data.append(hfac)
            rows.append(G(i, j))
            cols.append(G(i, j + 1))

            rhs[G(i, j)] = rhs_func(x[i], y[j])
        else:
            # Boundary, append zero Dirichlet condition.
            data.append(1)
            rows.append(G(i, j))
            cols.append(G(i, j))
            rhs[G(i, j)] = 0

matr = scipy.sparse.coo_array((data, (rows, cols)))
matr = scipy.sparse.csr_array(matr)  # Convert as required by `spsolve()`.

# Solve the linear system.
u = scipy.sparse.linalg.spsolve(matr, rhs)

# Reshape 1D array to 2D array.
uu = np.zeros((nx, nx))
for i in range(nx):
    for j in range(ny):
        uu[i, j] = u[G(i, j)]

'''
fig, ax = plt.subplots(figsize=(3.5, 3.5), subplot_kw={
    'projection': '3d',
})
xx, yy = np.meshgrid(x, y)
surf = ax.plot_surface(xx,
                       yy,
                       uu,
                       cmap='jet',
                       rstride=1,
                       cstride=1,
                       linewidth=0.1,
                       edgecolors='k')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
fig.savefig('poisson.pdf', bbox_inches='tight')
fig.savefig('poisson.svg', bbox_inches='tight')
plt.close(fig)
'''

plt.rcParams.update({
    "axes.spines.left": True,
    "axes.spines.right": True,
    "axes.spines.top": True,
    "axes.spines.bottom": True,
})
fig, ax = plt.subplots()
ax.spy(matr, marker='s', markersize=2)
fig.savefig('poisson_spy.svg')
