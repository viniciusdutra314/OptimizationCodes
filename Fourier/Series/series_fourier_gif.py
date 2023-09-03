import scipy.integrate as integrate
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
def function(t):
    return t**3+np.exp(t)
def fourier_function(t, a_coefficients, b_coefficients, L):
    value=a_coefficients[0]/2
    for n in range(1, len(a_coefficients)):
        value += a_coefficients[n] * np.cos(n * np.pi * t / L)
        value += b_coefficients[n] * np.sin(n * np.pi * t / L)
    return value
def fourier_coefficients(function : callable, N_terms : int = 100, L = 1):
  a_coefficients = np.empty(N_terms)
  b_coefficients = np.empty(N_terms)
  a0 = (1 / L) * integrate.quad(function, -L, L)[0]
  a_coefficients[0] = a0
  for n in range(0, N_terms):
      a_coefficients[n] = (1 / L) * integrate.quad(lambda t: function(t) * np.cos(n * np.pi * t / L), -L, L)[0]
      b_coefficients[n] = (1 / L) * integrate.quad(lambda t: function(t) * np.sin(n * np.pi * t / L), -L, L)[0]
  return a_coefficients, b_coefficients
N_terms = 100
L = 3
t = np.linspace(-L, L, 1000)
writer=PillowWriter(fps=5)
fig ,axis= plt.subplots()
with writer.saving(fig,'fourier_series.gif',100):
    for N in range(1,N_terms):
        a_coefficients, b_coefficients=fourier_coefficients(function,N_terms=N,L=L)
        y =np.array([fourier_function(tempo, a_coefficients, b_coefficients, L) for tempo in t])
        axis.plot(t,y,label=f"Fourier series N={N}")
        axis.plot(t,function(t),label=f"Function",alpha=0.5)
        axis.legend()
        writer.grab_frame()
        axis.clear()
