import numpy as np
import matplotlib.pyplot as plt
from receive_args_alg import get_args
data, start, end = get_args()
start=int(start)
end=int(end)
N=len(data)

def total_distance(sequence, data):
    return np.sum(data[sequence[:-1], sequence[1:]])
@np.vectorize
def random_sequence(N,start,end):
    permutar = [j for j in range(N) if j not in [start, end]]
    permutacao=np.random.permutation(permutar)
    return np.array([start] + list(permutacao) + [end])
@np.vectorize
def update_temperature(iteration,max_iterations,t0,alpha):
    return t0*np.exp(-alpha*iteration/max_iterations)
def random_reverse(seq):
    x = np.copy(seq)
    length = np.random.randint(2, len(seq) - 2)
    index = np.random.choice(np.arange(1, len(x)-1), replace=False)
    index_end = index + length

    seq_start = x[:index]
    seq_middle = x[index:index_end][::-1]
    seq_end = x[index_end:]
    
    return np.concatenate([seq_start, seq_middle, seq_end])


def random_swap(seq):
    x=np.copy(seq)
    times=np.random.randint(1,len(seq))
    for _ in range(times):
        index_a, index_b = np.random.choice(
            list(range(len(x)))[1:-1], 2, replace=False)
        x[index_a], x[index_b] = x[index_b], x[index_a]
    return x



def calculate_delta_E(data, seq1, seq2) -> float:
    mask = (seq1[:-1] != seq2[:-1]) | (seq1[1:] != seq2[1:])
    elements_A = seq1[:-1][mask]
    elements_B = seq2[:-1][mask]
    delta_E = np.sum(data[elements_A, seq1[1:][mask]]) - np.sum(data[elements_B, seq2[1:][mask]])
    return delta_E

@np.vectorize
def run_annealing(t0,alpha):
    NUM_ITERATIONS=int(1E4)
    mean=5
    costs=np.zeros(mean)
    for j in range(mean):
        costs[j]=np.inf
        sequence=random_sequence(N,start,end)
        for i in range(NUM_ITERATIONS):
            temperature=update_temperature(i,NUM_ITERATIONS,t0,alpha)
            new_sequence=random_reverse(sequence)
            delta_E=calculate_delta_E(data,new_sequence,sequence)
            if delta_E<0:  sequence=new_sequence
            else:
                if np.random.rand() <np.exp(-delta_E / temperature):
                    sequence=new_sequence
        costs[j]=total_distance(sequence,data)
    return np.mean(costs)
t0=np.linspace(1e-1,1,30)
alpha=np.linspace(1e-1,1,30)
t0,alpha=np.meshgrid(t0,alpha)
import cProfile
import pstats
#prof=cProfile.Profile()
#prof.enable()
Z=run_annealing(t0,alpha)
#prof.disable()
#stats=pstats.Stats(prof).sort_stats('tottime')
#stats.print_stats()
fig,axis=plt.subplots(figsize=(8,6))
plt.style.use('ggplot')
img=axis.imshow(Z,extent=(np.min(alpha),np.max(alpha),
                np.min(t0),np.max(t0)),aspect=np.max(alpha)/np.max(t0))
axis.set_xlabel(r'Alpha value $\alpha$')
axis.set_ylabel(r'Initial temperature $T_0$')
fig.colorbar(img,ax=axis)
fig.savefig('teste.jpg',dpi=200,bbox_inches='tight')
