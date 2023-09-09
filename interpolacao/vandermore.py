import numpy as np
import matplotlib.pyplot as plt
N=4
pontos_x,pontos_y=np.random.uniform(size=(2,N))
vander_matrix=np.vander(pontos_x) #v_ij=(x_i)^j
coeficientes=np.linalg.inv(vander_matrix).dot(pontos_y)
polinomio=np.polynomial.Polynomial(coef=coeficientes[::-1])
x=np.linspace(0,1,100)
fig,axis=plt.subplots()
axis.scatter(pontos_x,pontos_y,label="Pontos")
axis.plot(x,polinomio(x),label=f"Polinomio grau {N-1}",color='g')
axis.grid()
axis.legend()
fig.savefig("vandermore.png")