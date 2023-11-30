

import numpy as np

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
    def __getitem__(self,item):
        return self.gene[item]

def random_reverse(individual : Individual) -> Individual:
    x=list(np.copy(individual.gene))
    length=np.random.randint(2,len(individual)-2)
    while True:
        index=np.random.choice(list(range(len(x)))[1:-1], replace=False)
        if index+length<=len(x)-2:
            break
    gene_start=x[:index]
    gene_middle=x[index:index+length][::-1]
    gene_end=x[index+length:]
    return Individual(np.array(gene_start+gene_middle+gene_end))

def random_swap(individual: Individual) -> Individual:
    x=np.copy(individual.gene)
    times=np.random.randint(1,len(individual))
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
    indices=np.random.choice(a=len(IndividualArray),p=chances,size=num_individuals)
    survived=np.zeros(shape=(NUM_INDIVIDUALS,len(IndividualArray[0])),dtype=int)
    for index,survival in enumerate(indices): survived[index]=IndividualArray[survival]
    return survived

def assexual_reproduction(IndividualArray : list[Individual]) -> list[Individual]:
    return IndividualArray
def partially_mapped_crossover(parents : list[Individual]):
    parents=np.delete(parents,[0,-1],axis=1)
    gene_size=len(parents[0])
    NUM_INDIVIDUALS=len(parents)
    start_cut,end_cut = sorted(np.random.default_rng().choice(
                        gene_size, size=2, replace=False))
    offsprings=np.zeros(shape=(NUM_INDIVIDUALS,gene_size),dtype=int)
    for i in range(NUM_INDIVIDUALS//2):
        start_cut,end_cut=10,16
        mapping={parents[2*i][j]:parents[2*i+1][j] for j in range(start_cut,end_cut)}
        reverse_mapping={parents[2*i+1][j]:parents[2*i][j] for j in range(start_cut,end_cut)}
        offsprings[2*i][start_cut:end_cut]=parents[2*i+1][start_cut:end_cut]
        offsprings[2*i+1][start_cut:end_cut]=parents[2*i][start_cut:end_cut]
        for j in range(2):
            for index,element in enumerate(parents[2*i+j]):
                if not (start_cut<=index<end_cut):
                    if element not in offsprings[2*i+j]:
                        offsprings[2*i+j][index]=element
        for j in range(2):
            for index,number in enumerate(offsprings[2*i+j]):
                if number==0:
                    element=parents[2*i+j][index]
                    visited=[element]
                    while True:
                        if element in mapping:
                            next_element=mapping[element]
                            if  next_element not in visited:
                                visited.append(next_element)
                                element=next_element
                                if element not in offsprings[2*i+j]: break
                        if element in reverse_mapping:
                            next_element=reverse_mapping[element]
                            if  next_element not in visited:
                                visited.append(next_element)
                                element=next_element
                                if element not in offsprings[2*i+j]: break
                    offsprings[2*i+j][index]=element
    return offsprings
NUM_GENERATIONS = 1000
NUM_INDIVIDUALS=100
SWAP_RATE=0.4
REVERSE_RATE=0.1
individuals=[Individual() for _ in range(NUM_INDIVIDUALS)]
possibilites=[random_swap,random_reverse,lambda x: x]
p=[SWAP_RATE,REVERSE_RATE]
p=p+[1-sum(p)]
random_event=np.random.choice(possibilites,p=p,size=NUM_INDIVIDUALS)
all_costs=np.zeros(shape=(NUM_GENERATIONS,NUM_INDIVIDUALS))
for i in range(NUM_GENERATIONS):
    all_costs[i]=[x.cost() for x in individuals]
    individuals=natural_selection(individuals,NUM_INDIVIDUALS)
    offsprings=partially_mapped_crossover(individuals)
    for index, event in enumerate(random_event):
        new_offspring=event(offsprings[index])
        if new_offspring.fitness()>offsprings[index].fitness():
            offsprings[index]=new_offspring
    individuals=offsprings
best_individual=np.max(individuals)
np.savetxt('visualização//all_costs.txt',all_costs)
print([best_individual.cost(),list(best_individual.gene)])
        