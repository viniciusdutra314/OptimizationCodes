import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
CAPACITY = 1000
MAX_ITERATIONS = 100000


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


value = 0
track_value = np.zeros(MAX_ITERATIONS, dtype=int)
for i in range(MAX_ITERATIONS):
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
    new_value = total_value(seq)
    if value < new_value:
        value = new_value
    track_value[i] = value
assert (
    np.all(seq <= df['items']) and total_size(seq) < CAPACITY
), 'A Solução não é válida'
plt.style.use('ggplot')
plt.plot(track_value)
print(track_value[-1])
plt.xlabel('Iteração')
plt.ylabel('Value')
plt.title(f'Método random (value={track_value[-1]})')
plt.savefig('plot_random_search.jpg', dpi=200)
