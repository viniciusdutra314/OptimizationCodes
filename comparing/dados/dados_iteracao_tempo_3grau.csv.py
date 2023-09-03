from metodos import newton,halley, gerar_raizes
from numpy.polynomial import polynomial, Polynomial
from numpy.random import normal,random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial","Distancia","Convergiu"]
num_elements=1_000
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
for i in range(1_000):
        polinomio=Polynomial(random(3+1))
        x0=random()
        newton_results[i]=newton(x0,polinomio,epsilon=1e-9,distancia=1)
        halley_results[i]=halley(x0,polinomio,epsilon=1e-9,distancia=1)
df_newton=pd.DataFrame(data=newton_results,columns=columns)
df_halley=pd.DataFrame(data=halley_results,columns=columns)
filename='iteracao_tempo_3grau'
df_newton.to_csv(f"newton_{filename}.csv")
df_halley.to_csv(f"halley_{filename}.csv")