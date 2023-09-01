from numpy.polynomial import Polynomial
import numpy as np
import matplotlib.pyplot as plt

def newton(x0, func, grad, epsilon=1e-3, max_iter=100):
    iterations = 0
    while iterations < max_iter:
        x1 = x0 - func(x0) / grad(x0)
        iterations += 1
        if abs(x1 - x0) < epsilon:
            break
        x0 = x1
    return x0
newton=np.vectorize(newton)
polynomial = Polynomial([1, 0, 0,1])
derivative = polynomial.deriv(1)
xmin, xmax=-0.1,0.1
ymin, ymax=-0.1,0.1
X, Y=np.meshgrid(np.linspace(xmin,xmax,1000),np.linspace(ymin,ymax,1000))
complex_points=X+1j*Y
points=X+Y
converged = newton(x0=complex_points, func=polynomial, grad=derivative)
plt.imshow(np.imag(converged))
plt.savefig("Newton_fractal_zoom.png")