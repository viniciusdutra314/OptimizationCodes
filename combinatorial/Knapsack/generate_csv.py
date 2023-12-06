import pandas as pd
from numpy.random import randint
N=100
values=randint(0,100,size=N)
sizes=randint(1,10,size=N)
max_items=randint(1,10,size=N)
data = {'values': values, 'sizes': sizes, 'items': max_items}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)