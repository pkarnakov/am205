#!/usr/bin/env python3

import os
import wave
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100


def save_wav(path, data, rate=SAMPLE_RATE):
    data /= np.max(abs(data))
    data = (data * np.iinfo(np.int16).max).astype(np.int16)

    with wave.open(path, 'w') as obj:
        obj.setnchannels(1)  # Channels.
        obj.setsampwidth(2)  # Bytes per sample.
        obj.setframerate(rate)
        obj.writeframesraw(data)


def solve_wave(x, t, u_init, ut_init, rhs):
    """
    Solves the wave equation with zero Dirichlet conditions.
    """
    u = np.zeros((len(t), len(x)))
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    u[0] = u_init

    # First time step, second-order accurate.
    u_xx = (np.roll(u[0], -1) - 2 * u[0] + np.roll(u[0], 1)) / dx**2
    u_tt = u_xx + rhs[0]
    u[1] = u[0] + ut_init * dt + 0.5 * u_tt * dt**2

    # Further time steps.
    for n in range(1, len(t) - 1):
        u_xx = (np.roll(u[n], -1) - 2 * u[n] + np.roll(u[n], 1)) / dx**2
        u_tt = u_xx + rhs[n]
        # Bounary values remain unchanged.
        u[n + 1, 1:-1] = 2 * u[n, 1:-1] - u[n - 1, 1:-1] + u_tt[1:-1] * dt**2
    return u


x = np.linspace(0, 1, 100)
dx = x[1] - x[0]
dt = dx * 0.25
duration = 1  # Seconds.
tmax = duration * dt * SAMPLE_RATE
t = np.arange(0, tmax, dt)

# Zero initial derivatives and RHS.
ut_init = np.zeros_like(x)
rhs = np.zeros((len(t), len(x)))

# Initial value.
#u_init = np.sin(2 * x * 2 * np.pi)
#u_init += np.sin(3 * x * 2 * np.pi)
u_init = np.sin(x**3 * np.pi)

u = solve_wave(x, t, u_init, ut_init, rhs)

ux = (u[:, 1:] - u[:, :-1]) / dx
sound = np.mean(ux**2, axis=1)  # Approximation for string length.
sound -= sound[0]  # Start from zero.

save_wav("wave_audio.wav", sound)
