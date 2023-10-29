import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def function(t):
    return t**2+t

def fourier_function(t, A, phi, L):
    N_terms = len(A)
    result = np.zeros_like(t)
    for n in range(N_terms):
        result += A[n] * np.cos(np.pi * n * t / L - phi[n])
    return result

def fourier_coefficients(function, N_terms=100, L=1):
    a_coefficients = np.empty(N_terms)
    b_coefficients = np.empty(N_terms)
    phi = np.empty(N_terms)
    A = np.empty(N_terms)

    a0 = (1 / L) * integrate.quad(function, -L, L)[0]
    a_coefficients[0] = a0

    for n in range(1, N_terms):
        a_coefficients[n] = (1 / L) * integrate.quad(lambda t: function(t) * np.cos(n * np.pi * t / L), -L, L)[0]
        b_coefficients[n] = (1 / L) * integrate.quad(lambda t: function(t) * np.sin(n * np.pi * t / L), -L, L)[0]

    A = np.sqrt(a_coefficients**2 + b_coefficients**2)
    phi = np.arctan(-b_coefficients/a_coefficients)

    return A, phi

N_terms = 100
L = 1
t = np.linspace(-L, L, 1000)
writer = PillowWriter(fps=5)
fig, axis = plt.subplots(ncols=3, nrows=1, figsize=(15, 5))

with writer.saving(fig, 'fourier_series.gif', 100):
    A, phi = fourier_coefficients(function, N_terms=N_terms, L=L)
    for N in range(1, N_terms):
        y = fourier_function(t, A[:N], phi[:N], L)
        fig.suptitle(r"Série de Fourier da função $y(t)=t^2$")
        axis[0].plot(t, y, label=f"Fourier series N={N}")
        axis[0].plot(t, function(t), label=f"Function", alpha=0.5)
        axis[0].set_xlabel("Tempo")
        axis[0].set_ylabel(r"$f(t)$")

        axis[1].plot(range(1, N + 1), A[:N], label=r"$A_n$", color='g')
        axis[1].set_xlabel("Amplitude (n)")
        axis[1].set_xlim(0,N_terms)

        axis[2].plot(range(1, N + 1), phi[:N], label=r"$\phi_n$", color='r')
        axis[2].set_xlabel("Fase (n)")
        axis[2].set_xlim(0,N_terms)

        for ax in axis:
            ax.grid()
            ax.legend()

        writer.grab_frame()
        for ax in axis:
            ax.clear()
