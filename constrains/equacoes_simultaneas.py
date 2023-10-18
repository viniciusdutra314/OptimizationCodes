import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
func1=lambda x: np.exp(x[1])+x**2-5*x[0]
func2=lambda x: x[0]**2 -x[1] -x[1]**2
func=lambda x: func1(x)**2+func2(x)**2
raizes=[]
x_range=np.linspace(-5,5,100)
y_range=np.linspace(-5,5,100)
for x in x_range:
    for y in y_range:
        raiz=scipy.optimize.root(func,x0=[x,y],tol=1e-14)
        if raiz.success:
            if list(raiz.x) not in raizes:
                raizes.append(list(raiz.x))
breakpoint()











