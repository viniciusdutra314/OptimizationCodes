import argparse
import os
from itertools import permutations
from subprocess import run

import numpy as np
import pandas as pd
diretorio=os.path.join(os.getcwd(),'run_folder')
arquivo=[file for file in os.listdir(diretorio) if file.endswith('.csv')]
assert len(arquivo)==1 , "Mais de uma base de dados selecionada na run_folder"
arquivo=os.path.splitext(arquivo[0])[0]

coordinates = pd.read_csv(f'run_folder//{arquivo}.csv')
distances = np.loadtxt(f'run_folder//matriz_{arquivo}.txt')

parser = argparse.ArgumentParser()
parser.add_argument("start", help='Cidade inicial')
parser.add_argument("end")
args = parser.parse_args()
name_to_row = {coordinates['Cidade'][j]
    : j for j in range(coordinates['Cidade'].size)}
start = name_to_row[args.start]
end = name_to_row[args.end] if args.end != None else start

N = distances.shape[0]
shortest_path = [np.infty, ()]
permutar=list(range(N))
if start in permutar:permutar.remove(start)
if end in permutar:permutar.remove(end)
for permutacao in permutations(permutar, len(permutar)):
    permutacao = [start] + list(permutacao) + [end]
    total_path = np.sum([distances[permutacao[i]][permutacao[i+1]]
                            for i in range(len(permutacao)-1)])
    if total_path < shortest_path[0]:
            shortest_path = [total_path, permutacao]


with open(f'detalhes_caminhos//{args.start} {args.end} {arquivo}.txt','w') as txt:
    txt.write(f"Caminho mínimo de {shortest_path[0]}km\n\n")
    txt.write(f"Fazendo esse trajeto:\n")
    for index in range(len(shortest_path[1])-1):
        point_a = shortest_path[1][index]
        point_b = shortest_path[1][index+1]
        txt.writelines(f"{coordinates['Cidade'][point_a]} -> "
                       f"{coordinates['Cidade'][point_b]} "
                       f"{distances[point_a][point_b]}km\n\n")
        
        
assert shortest_path[1][0] == start
assert shortest_path[1][-1] == end
command = ['python3', 'plot_mapa.py',
           str(shortest_path[0])]
command += [str(number) for number in shortest_path[1]]
run(command, text=True)
