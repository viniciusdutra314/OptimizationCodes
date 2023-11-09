import numpy as np
import pandas as pd
from rich import print
from itertools import permutations
from datetime import timedelta
durations=np.loadtxt('matriz_campus.txt')
coordinates=pd.read_csv('campus_usp.csv')
N=durations.shape[0]
shortest_path=[np.max(durations)*N,()]
for permutacao in permutations(range(N),N):
    total_path=np.sum([durations[permutacao[i]][permutacao[i+1]]for i in range(N-1)])
    if total_path<shortest_path[0]: shortest_path=[total_path,permutacao]
print(f"Caminho mínimo de {timedelta(seconds=shortest_path[0])}")
print("")
print(f"Fazendo esse trajeto:")
for index in range(len(shortest_path[1])-1):
    start=shortest_path[1][index]
    end=shortest_path[1][index+1]
    print(f"{coordinates['Campus'][start]} -> "
          f"{coordinates['Campus'][end]} "
          f"{timedelta(seconds=durations[start][end])}")
    print("")