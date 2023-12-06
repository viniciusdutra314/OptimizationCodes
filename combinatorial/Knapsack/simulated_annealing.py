import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
CAPACITY=1000
MAX_ITERATIONS=10000
T0=1; ALPHA=3/MAX_ITERATIONS
temperature=T0
def update_temperature(iteration):
    global T0,ALPHA
    return T0*np.exp(-ALPHA*iteration)
def total_value(combination):
    global df
    assert len(combination)==len(df) , 'Tamanhos incompatíveis '\
    'entre combinação e dados'
    return np.dot(df['values'],combination)
def total_size(combination):
    global df
    assert len(combination)==len(df) , 'Tamanhos incompatíveis '\
    'entre combinação e dados'
    return np.dot(df['sizes'],combination)
while True:
    seq=np.random.choice([0,1],len(df))
    if total_size(seq)<CAPACITY:
        value_seq=total_value(seq)
        break
value=np.zeros(MAX_ITERATIONS,dtype=int)
for index in range(MAX_ITERATIONS):
    temperature=update_temperature(index)
    random_sub,random_add=np.random.randint(len(df),size=2)
    new_seq=np.copy(seq)
    if new_seq[random_sub]>0:
        new_seq[random_sub]-=1
    if new_seq[random_add]<df['sizes'][random_add]:
        new_seq[random_add]+=1
    fitness_newseq=total_value(new_seq)
    if total_size(new_seq)<CAPACITY:
        if fitness_newseq>value_seq:
            seq=new_seq; value_seq=fitness_newseq
        else:
            deltaE=fitness_newseq-value_seq
            if np.exp(deltaE/temperature)>np.random.random():
                seq=new_seq; value_seq=fitness_newseq
    value[index]=value_seq
print(seq)
print(f"value_seq = {value_seq}")
print(f"size = {total_size(seq)}")
print(f"Max size = {CAPACITY}")
plt.style.use('ggplot')
plt.plot(value)
plt.xlabel('Iteração')
plt.ylabel('Value')
plt.title(f'Método SA, (value={value[-1]})')
plt.savefig('plot_SA.jpg',dpi=200)