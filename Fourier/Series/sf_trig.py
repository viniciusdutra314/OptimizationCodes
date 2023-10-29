import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
def function(t):
    return (2*t)
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
L = 1
t = np.linspace(-L, L, 1000)
writer=PillowWriter(fps=5)
fig ,axis= plt.subplots(ncols=3,nrows=1,figsize=(15,5))
with writer.saving(fig,'fourier_series.gif',100):
    a_coefficients, b_coefficients=fourier_coefficients(function,N_terms=N_terms,L=L)
    for N in range(1,N_terms):
        y =np.array([fourier_function(tempo, a_coefficients[:N], b_coefficients[:N], L) for tempo in t])
        fig.suptitle(r"Série de fourier da função $y(t)=sin(t**2)+t$")
        axis[0].plot(t,y,label=f"Fourier series N={N}")
        axis[0].plot(t,function(t),label=f"Function",alpha=0.5)
        axis[0].set_xlabel("tempo")
        axis[0].set_ylabel(r"f(tempo)")
        axis[1].plot(range(len(a_coefficients)),a_coefficients,label=r"$a_n$",color='g')
        axis[1].set_xlabel("Nº termo")
        axis[2].plot(range(len(b_coefficients)),b_coefficients,label=r"$b_n$",color='r')
        axis[2].set_xlabel("Nº termo")
        for ax in axis:
            ax.grid()
            ax.legend()
        writer.grab_frame()
        for ax in axis:ax.clear()