import numpy as np
import matplotlib.pyplot as plt
from receive_args_alg import get_args
data, start, end = get_args()
start=int(start)
end=int(end)
N=len(data)
def total_distance(sequence, data):
    indices = np.array(sequence)
    return np.sum(data[indices[:-1], indices[1:]])
def random_sequence(N,start,end):
    permutar = [j for j in range(N) if j not in [start, end]]
    permutacao=np.random.permutation(permutar)
    return [start] + list(permutacao) + [end]
def update_temperature(iteration,max_iterations):
    T0=1; alpha=3/max_iterations
    return T0*np.exp(-alpha*iteration)
def random_reverse(seq):
    x=list(np.copy(seq))
    length=np.random.randint(2,len(seq)-2)
    while True:
        index=np.random.choice(list(range(len(x)))[1:-1], replace=False)
        if index+length<=len(x)-2:
            break
    seq_start=x[:index]
    seq_middle=x[index:index+length][::-1]
    seq_end=x[index+length:]
    return seq_start+seq_middle+seq_end
def random_swap(seq):
    x=np.copy(seq)
    times=np.random.randint(1,len(seq))
    for _ in range(times):
        index_a, index_b = np.random.choice(
            list(range(len(x)))[1:-1], 2, replace=False)
        x[index_a], x[index_b] = x[index_b], x[index_a]
    return x

def delta_E(seq1,seq2)-> float


NUM_ITERATIONS=int(1E5)
costs=np.zeros(NUM_ITERATIONS+1)
acceptance=np.zeros(NUM_ITERATIONS)
costs[0]=np.inf
sequence=random_sequence(N,start,end)
for i in range(NUM_ITERATIONS):
    temperature=update_temperature(i,NUM_ITERATIONS)
    new_sequence=random_reverse(sequence)
    delta_E=total_distance(new_sequence,data)-costs[i]
    if delta_E<0: sequence=new_sequence
    else:
        acceptance[i]=np.exp(-delta_E / temperature)
        if np.random.rand() <acceptance[i]:
            sequence=new_sequence
    costs[i+1]=total_distance(sequence,data)
print([costs[-1],list(sequence)])

ITERATIONS=range(NUM_ITERATIONS)
plt.style.use('ggplot')
figure,ax=plt.subplots(1,3,figsize=(15,5))
ax[0].plot(ITERATIONS,costs[1::])
ax[0].set_ylabel('Total distance')
ax[1].plot(ITERATIONS,
           update_temperature(ITERATIONS,NUM_ITERATIONS),
           color='blue')
ax[1].set_ylabel('Temperature')
ax[2].scatter(ITERATIONS,acceptance,s=0.3,color='green')
ax[2].set_ylabel('Acceptance probability')
for axis in ax:
    axis.set_xlabel('Num iterations')
    axis.grid()
figure.savefig('annealing.jpg',dpi=200)