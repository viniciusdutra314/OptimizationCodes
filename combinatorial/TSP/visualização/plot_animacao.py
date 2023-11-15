import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from receive_args_view import get_args

shortestpath, coords, data, start, end = get_args()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  

permutations = np.loadtxt('temp_iterations.txt')
max_value=permutations[0][-1]
min_value=permutations[-1][-1]
total_values = [permutation[-1] for permutation in permutations]
N=len(permutations)
def update(frame):
    ax1.clear()  
    ax2.clear()
    permutation = permutations[frame]
    total_value = permutation[-1]
    permutation = permutation[:-1]
    x = [coords['Latitude'][j] for j in permutation]
    y = [coords['Longitude'][j] for j in permutation]
    
    ax1.plot(x, y, label='Caminhos', linestyle='dashed')
    ax1.scatter(x[1:-1], y[1:-1], label='Pontos', color='red')
    ax1.scatter(x[0], y[0], label='Começo', color='purple')
    if (x[0], y[0]) != (x[-1], y[-1]):
        ax1.scatter(x[-1], y[-1], label='Fim', color='green')
    ax1.grid()
    ax1.legend()

    ax2.set_xlim(0,N)
    ax2.set_ylim(min_value,max_value)
    ax2.plot(range(frame + 1), total_values[:frame + 1],color='blue')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Total Value')
    ax2.grid()

animation = FuncAnimation(fig, update, 
                          frames=len(permutations), interval=500)

animation.save('animated_plot.gif', writer='pillow',fps=5,dpi=100)
plt.show()
