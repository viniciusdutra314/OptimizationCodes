from itertools import permutations
import numpy as np
from receive_args_alg import get_args
data,start,end=get_args()

N = len(data)
shortest_path = [np.infty, ()]
permutar=[j for j in range(N) if j not in [start,end]]

for permutacao in permutations(permutar, len(permutar)):
    permutacao = [start] + list(permutacao) + [end]
    total_path = np.sum([data[permutacao[i]][permutacao[i+1]]
                            for i in range(len(permutacao)-1)])
    if total_path < shortest_path[0]:
            shortest_path = [total_path, permutacao]
print(shortest_path)
                