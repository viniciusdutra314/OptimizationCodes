import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import minimize
durations=np.loadtxt('duracoes.txt')
durations=durations/np.max(durations)
N=durations.shape[0]
for i in range(N):
    for j in range(N):
        durations[i][j]=durations[j][i]
times=0
def geometric_error(coordinates):
    global N,durations,times
    times+=1
    x,y=coordinates.reshape(2,N)
    erro=0
    for i in range(N):
        for j in range(N):
            erro+=(np.hypot(x[i]-x[j],y[i]-y[j])-durations[i][j])**2
    print(f"{times} e {erro}")
    return erro
root=minimize(geometric_error, np.zeros(2*N))
x,y=(root.x).reshape(2,N)
plt.style.use('ggplot')
plt.scatter(x,y)
plt.savefig('UK.jpg',dpi=400)
breakpoint()