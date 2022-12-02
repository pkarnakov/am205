#!/usr/bin/env python3

import os
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from util_cache import cache_to_file
from util import get_path, savefig

SAMPLE_RATE = 48000


def save_wav(path, data, rate=SAMPLE_RATE):
    data *= 0.8 / np.max(abs(data))
    data = (data * np.iinfo(np.int16).max).astype(np.int16)
    scipy.io.wavfile.write(path, rate, data)


@cache_to_file("solve.pickle")
def solve_wave(x, t, u_init, ut_init, rhs):
    """
    Solves the wave equation with second order finite differences
    with zero Dirichlet conditions.
    """
    res_u = np.zeros((len(t), len(x)))
    h = x[1] - x[0]
    dt = t[1] - t[0]
    u = u_init
    res_u[0] = u

    u_xx = (np.roll(u, -1) - 2 * u + np.roll(u, 1)) / h**2
    u_tt = u_xx
    u_t = ut_init
    up = u + u_t * dt + 0.5 * u_tt * dt**2
    for n in range(1, len(t)):
        up[0] = 0
        up[-1] = 0
        res_u[n] = up
        um, u = u, up
        u_xx = (np.roll(u, -1) - 2 * u + np.roll(u, 1)) / h**2
        u_tt = u_xx + rhs[n]
        up = 2 * u - um + u_tt * dt**2
    return res_u


def run():
    nx = 128
    x = np.linspace(0, 1, nx)
    dx = x[1] - x[0]
    dt = dx * 0.23
    phys_tmax = 10.  # Duration in seconds.
    phys_dt = 1 / SAMPLE_RATE  # Time step in seconds.
    tmax = phys_tmax / phys_dt * dt
    t = np.arange(0, tmax, dt)
    phys_t = t * phys_tmax / tmax
    phys_tunit = phys_tmax / tmax
    phys_freq_1 = 60 # Hz.
    phys_freq_2 = 200 # Hz.
    freq_1 = phys_freq_1 * phys_tunit
    freq_2 = phys_freq_2 * phys_tunit

    u_init = np.zeros_like(x)
    ut_init = np.zeros_like(x)

    freq = freq_1 + (t / tmax) * (freq_2 - freq_1)
    phys_freq = freq / phys_tunit

    rhs = np.zeros((len(t), len(x)))
    rhs_base = np.where(x < 0.5, 1., 0.)  # Non-symmetric shape in space.
    rhs_base = 1 -  np.abs(x ** 2 - 0.5)
    rhs_base = x
    for n in range(len(t)):
        rhs[n] = rhs_base * np.sin(t[n] * freq[n] * np.pi * 2)

    u = solve_wave(x, t, u_init, ut_init, rhs)

    ux = (u[:, 1:] - u[:, :-1]) / dx
    data = np.mean(ux**2, axis=1)
    data -= data[0]
    gap = 8000 # Samples in head or tail.
    # Suppress head and tail to avoid clicks.
    if gap < len(data):
        data[:gap] *= np.linspace(0, 1, gap) ** 6
        data[-gap:] *= np.linspace(1, 0, gap) ** 6
    path = "wave_signal.wav"
    print(path)
    save_wav(path, data)

    data = np.mean(rhs, axis=1)
    if gap < len(data):
        data[:gap] *= np.linspace(0, 1, gap) ** 6
        data[-gap:] *= np.linspace(1, 0, gap) ** 6
    path = "wave_force.wav"
    print(path)
    save_wav(path, data)

    def downsample(t, v, nsmp=512):
        window = len(v) // nsmp
        t = t[:window * nsmp]
        v = v[:window * nsmp]
        t = np.mean(t.reshape((nsmp, window)), axis=1)
        v = np.mean(v.reshape((nsmp, window)), axis=1)
        return t, v

    fig, ax = plt.subplots()
    ut = (u[1:, :] - u[:-1, :]) / dt
    energy = np.mean(ut**2, axis=1)
    ax.set_xlabel('t [s]')
    ax.set_ylabel('energy (a.u.)', color='C0')
    ax2 = ax.twinx()
    ax2.spines['right'].set_visible(True)
    ax2.set_ylabel('force frequency [Hz]', color='C1')
    ax.plot(*downsample(phys_t, energy), c='C0', zorder=10)
    ax2.plot(*downsample(phys_t, phys_freq), c='C1', zorder=10)
    phys_eigenfreq = np.arange(3, 10) / phys_tunit / 4
    print("eigenfreq [Hz]: ", np.array_str(phys_eigenfreq, precision=3))
    for pf in phys_eigenfreq:
        i = np.argmin(np.abs(phys_freq - pf))
        ax2.axhline(y=pf, c='C1', lw=0.5, ls='--')
        ax2.axvline(x=phys_t[i], c='k', lw=0.5, ls='--')
    ax2.set_zorder(-5)
    ax2.set_ylim(0, phys_freq_2)
    fig.savefig("wave_energy.pdf")
    fig.savefig("wave_energy.svg")
    plt.close(fig)

    fps = 25
    for frame in range(int(fps * phys_tmax) + 1):
        path = "wave_{:04d}.png".format(frame)
        if os.path.isfile(path):
            print("skip existing '{:}'".format(path))
        else:
            fig, ax = plt.subplots()
            ptt = frame / fps
            it = np.argmin(np.abs(phys_t - ptt))
            ax.plot(x, u[it] / np.max(np.abs(u)))
            ax.set_axis_off()
            ax.set_ylim(-1.01, 1.01)
            ax.scatter([0, x.max()], [0, 0],
                       c='k',
                       clip_on=False,
                       zorder=5)
            print(path)
            fig.savefig(path, transparent=False)
            plt.close(fig)

    for frame in range(int(fps * phys_tmax) + 1):
        path = "wavesrc_{:04d}.png".format(frame)
        if os.path.isfile(path):
            print("skip existing '{:}'".format(path))
        else:
            fig, ax = plt.subplots()
            ptt = frame / fps
            it = np.argmin(np.abs(phys_t - ptt))
            ax.plot(x, rhs[it] / np.max(np.abs(rhs)), c='C1')
            ax.set_axis_off()
            ax.set_ylim(-1.01, 1.01)
            ax.axhline(y=0, c='k', lw=0.5, zorder=-1)
            print(path)
            fig.savefig(path, transparent=False)
            plt.close(fig)


run()
