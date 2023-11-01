from sympy import *
import numpy as np
from rich import print
simbolos=symbols('x y mu')
x,y,mu= simbolos ; n=len(simbolos)
eqs=Matrix([10*x**2+12*x*y +10*y**2 -4,cos(x*y)*y+mu*(5*x+12*y),
            cos(x*y)*x+mu*(5*y+12*x)])
vector=Matrix([1,1,0])
jac=Matrix.zeros(n,n)
epsilon=1e-8
max_interations=100
for i in range(n):
    for j in range(n):
        jac[i,j]=(diff(eqs[i],simbolos[j]))
def norm(vector):
    return sum([vec_comp**2 for vec_comp in vector])
def evalute(object,point):
    global simbolo
    dictionary={simbolo:value for simbolo,value in zip(simbolos,point)}
    return object.evalf(subs=dictionary)
times=0
while (norm(evalute(eqs,vector))>epsilon and times<max_interations):
    vector-=(evalute(jac,vector).inv()) * evalute(eqs,vector)
    times+=1
print(f"conjunto de equações:")
print(eqs)
print(f"Solução encontrado para epsilon={epsilon}")
print(vector)