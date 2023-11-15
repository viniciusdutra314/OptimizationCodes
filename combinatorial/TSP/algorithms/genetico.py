import argparse
import os
from subprocess import run

import numpy as np
import pandas as pd

from receive_args_alg import get_args

data, start, end = get_args()
start=int(start)
end=int(end)
class Individual:
    start = start
    end = end
    data = data

    def __init__(self, initial_permutation=None):
        if np.array_equal(initial_permutation, None):
            random_perm = np.random.permutation(
                [i for i in range(len(data)) if i not in [start, end]]
            )
            self.gene = np.concatenate(([start], random_perm, [end]))
        else:
            self.gene = initial_permutation

    def fitness(self) -> float:
        value=np.sum([data[self.gene[j]][self.gene[j + 1]]
                for j in range(len(self.gene) - 1)])
        return 1/value 
    def cost(self) -> float:
        value=np.sum([data[self.gene[j]][self.gene[j + 1]]
                for j in range(len(self.gene) - 1)])
        return value 
    def __le__(self, other):
        return self.fitness() <= other.fitness()

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __gt__(self, other):
        return self.fitness() > other.fitness()

    def __ge__(self, other):
        return self.fitness() >= other.fitness()

    def __str__(self):
        return str(self.gene)

    def __repr__(self):
        return str(self.gene)

    def __len__(self):
        return len(self.gene)


def random_reverse(individual : Individual, length : int=2) -> Individual:
    assert length <= len(individual)-2 , "Comprimento maior que gene"
    x=list(np.copy(individual.gene))
    while True:
        index=np.random.choice(list(range(len(x)))[1:-1], replace=False)
        if index+length<=len(x)-2:
            break
    gene_start=x[:index]
    gene_middle=x[index:index+length][::-1]
    gene_end=x[index+length:]
    return Individual(np.array(gene_start+gene_middle+gene_end))

def random_swap(individual: Individual,times: int =1) -> Individual:
    x=np.copy(individual.gene)
    for _ in range(times):
        index_a, index_b = np.random.choice(
            list(range(len(x)))[1:-1], 2, replace=False)
        x[index_a], x[index_b] = x[index_b], x[index_a]
    return Individual(x)

def natural_selection(IndividualArray : list[Individual],
              num_individuals :int=1) -> list[Individual]: 
    individual_fitness=np.array([individual.fitness() for individual in IndividualArray])
    total_fitness=np.sum(individual_fitness)
    chances=individual_fitness/total_fitness
    assert np.isclose(np.sum(chances),1) , "probabilidade total diferente de 1"
    return np.random.choice(IndividualArray,p=chances,size=num_individuals)
def assexual_reproduction(IndividualArray : list[Individual]) -> list[Individual]:
    return IndividualArray
def show_individuals_stats(IndividualArray : list[Individual]) -> None:
    IndividualArray=[x.cost() for x in IndividualArray]
    print("----")
    print(f"Min {np.min(IndividualArray)}")
    print(f"Média {np.mean(IndividualArray):.2f}")
    print(f"Desvio {np.std(IndividualArray):.2f}")
    print(f"Max {np.max(IndividualArray)}")
NUM_GENERATIONS = 1000
NUM_INDIVIDUALS=100
MUTATION_RATE=0.1
REVERSE_RATE=0.01
individuals=[Individual() for _ in range(NUM_INDIVIDUALS)]
possibilites=[random_swap,random_reverse,lambda x: x]
p=[MUTATION_RATE,REVERSE_RATE]
p=p+[1-sum(p)]
random_event=np.random.choice(possibilites,p=p,size=NUM_INDIVIDUALS)
show_individuals_stats(individuals)
for _ in range(NUM_GENERATIONS):
    individuals=natural_selection(individuals,NUM_INDIVIDUALS)
    offsprings=assexual_reproduction(individuals)
    for index, event in enumerate(random_event):
        offsprings[index]=event(offsprings[index])
    individuals=offsprings
show_individuals_stats(individuals)
        