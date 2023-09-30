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
        times+=1
        try:
            inversa=-np.linalg.inv(hessian(x))
        except np.linalg.LinAlgError:
            inversa=-np.linalg.inv(hessian(x*(1.01)))
        step= inversa@ grad(x)
        x+=step
        if func(x)<epsilon: break
    print(x)

newton((-35,1),func,grad,hessian)