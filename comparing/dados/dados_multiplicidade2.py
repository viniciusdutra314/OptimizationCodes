from metodos import newton,halley, gerar_raizes
from numpy.polynomial import polynomial, Polynomial
from numpy.random import normal,random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial","Distancia","Convergiu"]
num_elements=1_000*49
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
for j, grau in enumerate(range(1,50)):
    print(grau)
    for i in range(1_000):
        aleatorios=random(grau)
        coeficientes=polynomial.polyfromroots(np.concatenate((aleatorios,aleatorios)))
        polinomio=Polynomial(coeficientes)
        x0=random()
        newton_results[i+1_000*j]=newton(x0,polinomio,epsilon=1e-9,distancia=grau)
        halley_results[i+1_000*j]=halley(x0,polinomio,epsilon=1e-9,distancia=grau)
df_newton=pd.DataFrame(data=newton_results,columns=columns)
df_halley=pd.DataFrame(data=halley_results,columns=columns)
df_newton.to_csv("newton_multiplicidade2.csv")
df_halley.to_csv("halley_multiplicidade2.csv")