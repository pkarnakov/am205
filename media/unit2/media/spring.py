#!/usr/bin/env python3

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from util import savefig
import mpl_toolkits.mplot3d as a3

fig, ax = plt.subplots(figsize=(6, 10),
                       subplot_kw={
                           'projection': '3d',
                           'proj_type': 'ortho',
                           'computed_zorder': False,
                       })
ax.view_init(2, -90)
ax.set_box_aspect((2, 2, 2.3), zoom=1)
ax.set_axis_off()


def spring(x0=0, y0=0, z0=0, r=0.8, k=1, c='k'):
    t = np.linspace(0, 1, 2000)
    om = 41
    ph = np.pi * 0.2
    x = np.cos(ph + om * t) * r
    y = np.sin(ph + om * t) * r
    z = -t * k
    capt = 0.05
    cap = np.ones_like(t)
    cap = np.minimum(cap, ((t.max() - t) / capt)**2)
    cap = np.minimum(cap, (t / capt)**2)
    x *= cap
    y *= cap
    x += x0
    y += y0
    z += z0
    ax.plot(x, y, z, c=c)


def plate(x0=0, y0=0, z0=0, dx=1.5, dy=1, c='C6'):
    face = [[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]]
    angle = np.deg2rad(20)
    cos, sin = np.cos(angle), np.sin(angle)
    for p in face:
        p[0] = 2 * p[0] - 1
        p[1] = 2 * p[1] - 1
    for p in face:
        p[0], p[1] = cos * p[0] - sin * p[1], sin * p[0] + cos * p[1]
    for p in face:
        p[0] = x0 + dx * p[0]
        p[1] = y0 + dy * p[1]
        p[2] = z0 + p[2]
    face = a3.art3d.Poly3DCollection([face])
    face.set_color(c)
    face.set_edgecolor('k')
    face.set_zorder(5)
    face.set_linewidth(0.5)
    ax.add_collection3d(face)


def sphere(x0=0, y0=0, z0=0, r=0.8, mu=20, mv=10, c='C0'):
    u1 = np.linspace(0, 2 * np.pi, mu)
    v1 = np.linspace(0, np.pi, mv)
    u, v = np.meshgrid(u1, v1)
    x = x0 + r * np.cos(u) * np.sin(v)
    y = y0 + r * np.sin(u) * np.sin(v)
    z = z0 - r + r * np.cos(v)
    ax.plot_surface(x,
                    y,
                    z,
                    color=c,
                    edgecolor='none',
                    antialiased=False,
                    linewidth=0,
                    zorder=-5)


spring(x0=-4, k=2)
spring(x0=0, k=4)
spring(x0=4, k=8)
plate(x0=-4)
plate(x0=0)
plate(x0=4)

q = 2**(1 / 3)
q0 = 0.7
sphere(-4, 0, -2, r=q0)
sphere(0, 0, -4, r=q0 * q)
sphere(4, 0, -8, r=q0 * q**2)

savefig(fig, pad_inches=-1.)
plt.close(fig)
