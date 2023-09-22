import numpy as np
import matplotlib.pyplot as plt
def sf_complexa(t):
    global c_minus, c_plus
    value=0
    for index, coef in enumerate(c_minus):
        value+=coef*np.exp(-1j*t*(len(c_minus)-index))    
    for index, coef in enumerate(c_plus):
        value+=coef*np.exp(1j*index*t)    
    return value
t = np.linspace(-np.pi, np.pi, 1000)  
N = 10
a_n = np.random.random(N)
b_n=np.random.random(N);b_n[0]=0
c_plus = (a_n - 1j * b_n) / 2
c_minus = (a_n + 1j * b_n) / 2
c_minus=c_minus[::-1][:-1] #inverte a ordem e exclui o ultimo elemento
plt.plot(t, sf_complexa(t))
coeficientes=np.concatenate((c_minus,c_plus))
polinomio=np.polynomial.Polynomial(coeficientes)
roots_z=polinomio.roots()
for root in roots_z:
    x=np.angle(root)
    print(x)
    if np.isclose(sf_complexa(x),0,atol=1e-6):
        plt.scatter(x,sf_complexa(x),color='g')
plt.axhline(0, color='r', label="y=0")
plt.grid()
plt.legend()
plt.savefig("teste.png") 