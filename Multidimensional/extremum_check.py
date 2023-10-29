from sympy import *
import numpy as np 
from rich import print
simbolos=symbols('x y z')
x,y, z= simbolos
sympy_func=sin(x)*cos(y)*sin(z)
func=lambdify(simbolos,sympy_func,'numpy')
grad=np.array([(diff(sympy_func,simbolo)) for simbolo in simbolos])
n=len(simbolos)
hessian=np.zeros((n,n),dtype=object)
for i in range(n):
    for j in range(n):
        hessian[i][j]=(diff(sympy_func,simbolos[i],simbolos[j]))
def evalute_hessian(hessian,point):
    global simbolos
    return np.array([[lambdify(simbolos,entrada,modules='numpy')(*point)
                      for entrada in linha] for linha in hessian])
def evalute_grad(grad,point):
    global simbolos
    return np.array([lambdify(simbolos,entrada,modules='numpy')(*point)
                      for entrada in grad])

def definess(grad, matrix):
    eigen_values=np.linalg.eigvals(matrix)
    positive=eigen_values >= 0
    negative=eigen_values <= 0
    if np.any(np.abs(grad)>1e-6):
        return "Gradient different from zero"
    if np.all(positive):
        return "positive-defined (minimum)"
    if np.all(negative):
        return "negative-defined (maximum)"
    else:
        return "undefined"
point=(np.pi/2,0,np.pi/2)
hessian_calculated=evalute_hessian(hessian,point)
grad_calculated=evalute_grad(grad,point)
print(f"function {sympy_func}")
print(f"Gradiant:")
print(grad)
print(f"Hessian:")
print(hessian)
print(f"At the point {point} {definess(grad_calculated,hessian_calculated)}")

