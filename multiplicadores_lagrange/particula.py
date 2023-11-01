import numpy as np 
import matplotlib.pyplot as plt
import sympy as sp
def gradient_descent(func,grad,x0) -> list:
    max_int=100
    num_iterations=0
    iterations_x=[x0[0]]
    iterations_y=[x0[1]]
    while (num_iterations<max_int and abs(func(*x0))>1e-6):
        x0=x0-0.1*grad(*x0)
        num_iterations+=1
        iterations_x.append(x0[0])
        iterations_y.append(x0[1])
    return iterations_x,iterations_y
fig,ax=plt.subplots()
temp=np.sqrt(np.pi/2)
ax.scatter([-temp,-temp,temp,temp],[-temp,+temp,-temp,temp],
           label=r'Extremos da função $f(x)$',color='red')
mu_min=-0.1
mu_max=0
initial_point=np.array([0.4,0.4])
for mu in np.linspace(mu_min,mu_max,1000):
    func=lambda x,y: -np.sin(x*y) +mu*(10*x**2 +12*x*y +10*y**2 -4)
    grad=lambda x,y:-np.array([np.cos(x*y)*y+mu*(5*x+12*y),
                           np.cos(x*y)*x +mu*(5*y+12*x)])
    iterations_x, iterations_y=gradient_descent(func,grad,initial_point)
    sc=ax.scatter(iterations_x[-1],iterations_y[-1],alpha=0.4,
               c=mu, vmin=mu_min,vmax=mu_max)
ax.scatter(initial_point[0],initial_point[1],
           label='Ponto inicial',color='orange')
X,Y=np.meshgrid(np.linspace(-2,2,100),np.linspace(-2,2,100))
elipse=lambda x,y:10*x**2+12*x*y +10*y**2 -4
ax.contour(X,Y,elipse(X,Y),levels=[0],color='green')
ax.set_aspect('equal')
cbar=fig.colorbar(sc)
cbar.set_label(r'Variando o valor de $\mu$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.scatter(0.353,0.3535,label='Solução numérica',color='pink')
ax.legend(loc='upper center')
fig.savefig('teste.png')
