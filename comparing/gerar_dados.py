from metodos import newton,halley, gerar_raizes
from numpy.polynomial import polynomial, Polynomial
from numpy.random import normal,random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
columns=["x0","f(x0)","Iterações","Tempo","Epsilon","Valor inicial","Distancia"]
num_elements=1_000*50
newton_results=np.empty((num_elements,len(columns)))
halley_results=np.empty((num_elements,len(columns)))
for j, erro in enumerate(range(50)):
    print(erro)
    for i in range(1_000):
        raizes=gerar_raizes(grau=100,tipo="diferentes")
        coeficientes_polinomio=polynomial.polyfromroots(raizes)
        polinomio=Polynomial(coeficientes_polinomio)
        x=np.linspace(-1,1,100)
        plt.plot(x,polinomio(x))
        plt.yscale("log")
        plt.savefig("teste.png")
        breakpoint()
        derivada=polinomio.deriv(1)
        segunda_derivada=derivada.deriv(1)
        print(polinomio)
        x0=np.longdouble(random())
        newton_results[i+1_000*j]=newton(x0,polinomio,derivada,epsilon=erro,distancia=1)
        halley_results[i+1_000*j]=halley(x0,polinomio,derivada,segunda_derivada,epsilon=erro,distancia=1)
df=pd.DataFrame(data=newton_results,columns=columns)
df.to_csv("temporario//newton.csv")
df=pd.DataFrame(data=halley_results,columns=columns)
df.to_csv("temporario//halley.csv")