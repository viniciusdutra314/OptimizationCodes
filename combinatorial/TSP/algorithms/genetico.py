import pandas as pd
import numpy as np
from subprocess import run
import argparse
import os

from receive_args_alg import get_args
data,start,end=get_args()

num_generations=1000
class Genome:
    start=start
    end=end
    data=data
    def __init__(self,initial_permutation=None):
        if np.array_equal(initial_permutation,None):
            random_perm=np.random.permutation([i for i in range(len(data)) if 
                        i not in [start,end] ])  
            self.chromosome=np.concatenate(([start],random_perm,[end]))
        else:
            self.chromosome=initial_permutation
    def fitness(self) -> float:
        return np.sum([data[self.chromosome[j]]
                       [self.chromosome[j+1]] for j 
                       in range(len(self.chromosome)-1)])   
    def __le__(self,other):
        return self.fitness()<=other.fitness()
    def __lt__(self,other):
        return self.fitness()<other.fitness()
    def __gt__(self,other):
        return self.fitness()>other.fitness()
    def __ge__(self,other):
        return self.fitness()>=other.fitness()
    def __str__(self): return str(self.chromosome)
    def __repr__(self): return str(self.chromosome)
    def __len__(self): return len(self.chromosome)
def random_swap(gene : Genome) -> Genome:
    x=np.copy(gene.chromosome)
    index_a,index_b=np.random.choice(list(range(len(x)))[1:-1],2,replace=False)
    x[index_a], x[index_b]=x[index_b],x[index_a]
    new_gene=Genome(x)
    return new_gene if new_gene<gene else gene
random_swap=np.vectorize(random_swap)
genes=[Genome() for i in range(10)]
for generation in range(num_generations):
    genes=random_swap(genes)
minimal_gene=np.min(genes)
shortest_path=[minimal_gene.fitness(),minimal_gene.chromosome]
command = ['python3', 'cidades//plot_mapa.py',
           str(shortest_path[0])]
command += [str(number) for number in shortest_path[1]]
run(command, text=True)
