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
        polinomio=Polynomial(random(4+1))
        x0=random()*d
        newton_results[i+1_000*j]=newton(x0,polinomio,epsilon=1e-9,distancia=d)
        halley_results[i+1_000*j]=halley(x0,polinomio,epsilon=1e-9,distancia=d)
df_newton=pd.DataFrame(data=newton_results,columns=columns)
df_halley=pd.DataFrame(data=halley_results,columns=columns)
df_newton.to_csv("newton_distancia_4grau.csv")
df_halley.to_csv("halley_distancia_4grau.csv")