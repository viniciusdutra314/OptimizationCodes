import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
CAPACITY = 1000
MAX_ITERATIONS = 100000
T0 = 3
ALPHA = 3 / MAX_ITERATIONS
temperature = T0


def update_temperature(iteration):
    global T0, ALPHA
    return T0 * np.exp(-ALPHA * iteration)


def total_value(combination):
    global df
    assert len(combination) == len(df), (
        'Tamanhos incompatíveis ' 'entre combinação e dados'
    )
    return np.dot(df['values'], combination)


def total_size(combination):
    global df
    assert len(combination) == len(df), (
        'Tamanhos incompatíveis ' 'entre combinação e dados'
    )
    return np.dot(df['sizes'], combination)


# original random
indexes = np.random.choice(range(0, len(df)), size=len(df), replace=False)
seq = np.zeros(len(df), dtype=int)
temp_weight = 0
for index in indexes:
    rand_quantity = np.random.randint(0, df['items'][index])
    extra_weight = df['sizes'][index] * rand_quantity
    temp_weight += extra_weight
    if temp_weight < CAPACITY:
        seq[index] = rand_quantity
    else:
        break
value = np.zeros(MAX_ITERATIONS, dtype=int)
value_seq = total_size(seq)
for index in range(MAX_ITERATIONS):
    temperature = update_temperature(index)
    random_sub, random_add = np.random.randint(len(df), size=2)
    new_seq = np.copy(seq)
    # adding and subtract
    if new_seq[random_sub] > 0:
        new_seq[random_sub] -= 1
    if new_seq[random_add] < df['items'][random_add]:
        new_seq[random_add] += 1
    # random swap
    index_a, index_b = np.random.randint(len(df), size=2)
    if new_seq[index_a] < df['items'][index_b]:
        if new_seq[index_b] < df['items'][index_a]:
            new_seq[index_a], new_seq[index_b] = (
                new_seq[index_b],
                new_seq[index_a],
            )
    fitness_newseq = total_value(new_seq)
    if total_size(new_seq) < CAPACITY:
        if fitness_newseq > value_seq:
            seq = new_seq
            value_seq = fitness_newseq
        else:
            deltaE = fitness_newseq - value_seq
            if np.exp(deltaE / temperature) > np.random.random():
                seq = new_seq
                value_seq = fitness_newseq
    value[index] = value_seq
assert (
    np.all(seq <= df['items']) and total_size(seq) <= CAPACITY
), 'A Solução não é válida'
plt.style.use('ggplot')
plt.plot(value)
plt.xlabel('Iteração')
plt.ylabel('Value')
plt.title(f'Método SA, (value={value[-1]})')
plt.savefig('plot_SA.jpg', dpi=200)
