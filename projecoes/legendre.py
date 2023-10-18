import numpy as np
from numpy.polynomial import Polynomial
from scipy.special import legendre
from scipy.integrate import quad
import matplotlib.pyplot as plt
function=lambda x: np.cos(2*x)
taylor=lambda x: 1-((2*x)**2)/2 #+((4*x)**4)/24
poly_legendre=Polynomial(0)
order_max = 2
a_n=np.zeros(order_max+1)

for index,order in enumerate(range(order_max+1)):
    legendre_coeffs = list(legendre(order))[::-1]
    polinomio=Polynomial(legendre_coeffs)
    a_n[index] = quad(lambda x:polinomio(x)*function(x),-1,1)[0]    
    a_n /= 2 / (2 * index + 1)
    poly_legendre += a_n[index]*polinomio
    
print(poly_legendre)
x=np.linspace(-1,1,1000)
plt.style.use("seaborn-v0_8")
plt.plot(x,function(x),label=r"$f(x)$")
plt.ylim(-1.1,1.1)
plt.plot(x,poly_legendre(x),label=f"$Legendre \, \, N={order_max}$",alpha=0.7,color='r')
plt.plot(x,taylor(x),label=f"$Taylor \, \, N={order_max}$",alpha=0.7)
plt.legend()
plt.show()