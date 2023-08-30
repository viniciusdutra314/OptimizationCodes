from metodos import newton,halley, gerar_raizes
from numpy.polynomial import polynomial, Polynomial
from numpy.random import normal,random
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial","Distancia"]
num_elements=1_000*16
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
erros=[1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8,1e-9,1e-10,1e-11,1e-12,1e-13,1e-14,1e-15,1e-16]
for j, erro in enumerate(erros):
    print(erro)
    for i in range(1_000):
        raizes=gerar_raizes(grau=3,tipo="diferentes")
        coeficientes_polinomio=polynomial.polyfromroots(raizes)
        polinomio=Polynomial(coeficientes_polinomio)
        derivada=polinomio.deriv(1)
        segunda_derivada=derivada.deriv(1)
        x0=np.float256(random())
        newton_results[i+1_000*j]=newton(x0,polinomio,derivada,epsilon=erro,distancia=3)
        halley_results[i+1_000*j]=halley(x0,polinomio,derivada,segunda_derivada,epsilon=erro,distancia=3)
df=pd.DataFrame(data=newton_results,columns=columns)
df.to_csv("temporario//newton.csv")
df=pd.DataFrame(data=halley_results,columns=columns)
df.to_csv("temporario//halley.csv")