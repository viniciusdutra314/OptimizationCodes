from metodos import newton,halley, gerar_raizes
from numpy.polynomial import polynomial, Polynomial
from numpy.random import normal,random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial","Distancia","Convergiu"]
num_elements=1_000*50
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
for j, d in enumerate(range(50)):
    print(d)
    for i in range(1_000):
        polinomio=Polynomial(random(d+1))
        x0=random()
        newton_results[i+1_000*j]=newton(x0,polinomio,epsilon=1e-9,distancia=d)
        halley_results[i+1_000*j]=halley(x0,polinomio,epsilon=1e-9,distancia=d)
df_newton=pd.DataFrame(data=newton_results,columns=columns)
df_halley=pd.DataFrame(data=halley_results,columns=columns)
filename='grau_variavel'
df_newton.to_csv(f"newton_{filename}.csv")
df_halley.to_csv(f"halley_{filename}.csv")