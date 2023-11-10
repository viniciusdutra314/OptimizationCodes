import argparse
from itertools import permutations
from subprocess import run

import numpy as np
import pandas as pd

distances = np.loadtxt('dados//matriz_campus.txt')
coordinates = pd.read_csv('dados//campus_usp.csv')

parser = argparse.ArgumentParser()
parser.add_argument("start", help='Cidade inicial')
parser.add_argument("end",required=False)
args = parser.parse_args()
name_to_row = {coordinates['Campus'][j]
    : j for j in range(coordinates['Campus'].size)}
start = name_to_row[args.start]
end = name_to_row[args.end] if args.end != None else start

N = distances.shape[0]
shortest_path = [np.infty, ()]

for permutacao in permutations(range(N), N):
    permutacao = list(permutacao)
    if end == start:
        permutacao.append(end)
    if permutacao[0] == start and permutacao[-1] == end:
        total_path = np.sum([distances[permutacao[i]][permutacao[i+1]]
                            for i in range(len(permutacao)-1)])
        if total_path < shortest_path[0]:
            shortest_path = [total_path, permutacao]


with open(f'detalhes_caminhos//{args.start}{args.end}.txt','w') as txt:
    txt.write(f"Caminho mínimo de {shortest_path[0]}km\n\n")
    txt.write(f"Fazendo esse trajeto:\n")
    for index in range(len(shortest_path[1])-2):
        point_a = shortest_path[1][index]
        point_b = shortest_path[1][index+1]
        txt.writelines(f"{coordinates['Campus'][point_a]} -> "
                       f"{coordinates['Campus'][point_b]} "
                       f"{distances[point_a][point_b]}km\n\n")
        
        
assert shortest_path[1][0] == start
assert shortest_path[1][-1] == end
command = ['python3', 'plot_campus.py',
           str(shortest_path[0])]
command += [str(number) for number in shortest_path[1]]
run(command, text=True)
