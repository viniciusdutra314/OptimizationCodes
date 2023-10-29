import numpy as np


def func(point):
    x, y = point    
    return np.sin(x)*np.cos(y)

def grad(point):
    x , y =point
    grad_x = np.cos(x)*np.cos(y)
    grad_y = -np.sin(x)*np.sin(y)
    return np.array([grad_x, grad_y])

def hessian(point):
    x ,y =point
    hessian_matrix = np.array([[-np.cos(y)*np.sin(x), -np.cos(x)*np.sin(y)],
                                [-np.cos(x)*np.sin(y), -np.cos(y)*np.sin(x)]])
    return hessian_matrix

def newton(initial_guess,func, grad,hessian):
    iterations=100
    times=0
    epsilon=1e-7
    x=initial_guess
    while (times<iterations):
        print(x)
        times+=1
        inversa=-np.linalg.inv(hessian(x))
        step= inversa@ grad(x)
        x+=step
        if func(x)<epsilon: break


newton(np.array([34,15]),func,grad,hessian)