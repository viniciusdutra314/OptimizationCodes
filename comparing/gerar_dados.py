from metodos import newton,halley, gerar_raizes
from classe_polinomios import Polinomio
from numpy.random import normal,random
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial"]
num_elements=1_000 
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
for i in range(num_elements):
    raizes=gerar_raizes(grau=3,tipo="diferentes")
    polinomio=Polinomio(raizes=raizes)
    derivada=polinomio.derivada()
    segunda_derivada=derivada.derivada()
    x0=random()
    newton_results[i]=newton(x0,polinomio,derivada,epsilon=1e-7)
    halley_results[i]=halley(x0,polinomio,derivada,segunda_derivada,epsilon=1e-7)
df=pd.DataFrame(data=newton_results,columns=columns)
df.to_csv("temporario//newton.csv")
df=pd.DataFrame(data=halley_results,columns=columns)
df.to_csv("temporario//halley.csv")