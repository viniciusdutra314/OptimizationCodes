import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

N = 10
x = np.linspace(1, 10, N)
y = 6 * x * (1 + 0.1 * np.random.normal(size=N))+1
c = np.concatenate((np.zeros(2), np.ones(N)))
b_ne = np.concatenate((y, y))

inequacoes = []
for j in range(2):
    sign =1
    for i in range(N):
        variaveis = np.array([sign, x[i] * sign])
        variaveis_zeros = np.zeros(N)
        variaveis_zeros[i] = 1
        inequacoes.append(np.concatenate((variaveis, variaveis_zeros)))
inequacoes = np.vstack(inequacoes)
bounds = [(None, None)] *2 
bounds += [(0, None)] * (N) 
result = linprog(c, A_ub=inequacoes, b_ub=b_ne,bounds=bounds)
print(result.x)
plt.scatter(x,y)
plt.savefig('teste.png')