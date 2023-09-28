from scipy.linalg import hadamard
import numpy as np
import matplotlib.pyplot as plt; plt.style.use("seaborn-v0_8")
n=5
t=np.linspace(0,1,2**n)
dados=np.cos((2*np.pi*1)*t)
matrix=hadamard(2**n)
plt.plot(matrix @ dados)
plt.savefig("DHT.jpg",dpi=200)