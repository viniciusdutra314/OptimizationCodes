import numpy as np
import matplotlib.pyplot as plt
from receive_args_view import get_args

shortestpath, coords, data, start, end,algoritmo = get_args()
cost=np.loadtxt('visualização//all_costs.txt')
means=np.array([np.mean(cost[i]) for i in range(len(cost))])
stds=np.array([np.std(cost[i]) for i in range(len(cost))])
plt.grid()
plt.plot(range(len(means)),means,label='Média')
plt.fill_between(range(len(means)),means+2*stds,means-2*stds,
                 color='r',alpha=0.3,label=r'Médias $\pm 2\sigma$')
plt.title(f'Algoritmo {algoritmo}')
plt.xlabel('Gerações')
plt.ylabel('Custo')
plt.legend()
plt.savefig(f'cost_vs_time_{algoritmo}{start}{end}.jpg',dpi=200)