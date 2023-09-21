import numpy as np
import matplotlib.pyplot as plt
grau=4
x=np.arange(1,10+1)
coefs_real=[3,5,-3,0.7,9][::-1]
Polinomio_real=np.polynomial.Polynomial(coefs_real)
Y=Polinomio_real(x)*(1+0.2*np.random.random(10))
X=np.vander(x,N=grau+1)
pseudo_inverse=np.linalg.inv(np.transpose(X) @ X)
coefs=(pseudo_inverse @ np.transpose(X)) @ Y
polinomio_aproximado=np.polynomial.Polynomial(coefs[::-1])
plt.scatter(x,Y,color='red',label=f"Polinomio real com ruido {Polinomio_real}")
plt.plot(x:=np.linspace(0,11,1000),polinomio_aproximado(x),label=f"{polinomio_aproximado}")
plt.legend(fontsize="8")
plt.savefig("teste.png")