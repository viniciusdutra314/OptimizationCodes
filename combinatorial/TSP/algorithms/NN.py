from itertools import permutations

import numpy as np

from receive_args_alg import get_args

data, start, end = get_args()

N = len(data)

cidades_nao_visitadas = [j for j in range(N) if j not in [start, end]]
cidades_visitadas=np.zeros(len(cidades_nao_visitadas)+2,dtype=int)
cidades_visitadas[0]=start
cidades_visitadas[-1]=end
for i in range(len(cidades_nao_visitadas)):
    possibilidades=data[int(cidades_visitadas[i])]
    NN=[np.inf,0]
    for j in cidades_nao_visitadas:
        if possibilidades[j]<NN[0]:
            if possibilidades[j]>0:
                NN[1]=j
                NN[0]=possibilidades[j]
    cidades_visitadas[i+1]=NN[1]
    cidades_nao_visitadas.remove(NN[1])
fitness=np.sum([data[cidades_visitadas[i]][cidades_visitadas[i+1]] for i in range(len(cidades_visitadas)-1)])
print([fitness,list(cidades_visitadas)])
