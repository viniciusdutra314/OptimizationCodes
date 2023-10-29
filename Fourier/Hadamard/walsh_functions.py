from scipy.linalg import hadamard
import numpy as np
import matplotlib.pyplot as plt; plt.style.use("seaborn-v0_8")
from scipy.interpolate import interp1d

n = 3
t = np.linspace(0, 1, 2**n)
matrix = hadamard(2**n)
x = np.linspace(0, 1, 1000)

fig, axes = plt.subplots(2**(n-1), 2**(n-1), figsize=(10, 10))

for i in range(2**(n-1)):
    for j in range(2**(n-1)):
        vetor = matrix[i + j]
        y_interp = interp1d(t, vetor, kind='zero')
        axes[i, j].plot(x, y_interp(x), alpha=0.5)
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])
plt.savefig("walsh.jpg",dpi=200)