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
x,y=sp.symbols('x y')
func=-sp.sin(x*y) +mu*(x**2 +y**2 -1)
grad=lambda x,y:-np.array([np.cos(x*y)*y+2*x*mu,np.cos(x*y)*x + 2*x*mu])


temp=np.sqrt(np.pi/2)
ax.scatter([-temp,-temp,temp,temp],[-temp,+temp,-temp,temp],
           label=r'Extremos da função $f(x)$',color='red')
mu_min=-1
mu_max=0
initial_point=np.array([1,1])
x,y = np.meshgrid(np.linspace(-2,2,10),np.linspace(-2,2,10))
for mu in np.linspace(mu_min,mu_max,100):
    func=lambda x,y:-np.sin(x*y) +mu*(x**2 +y**2 -1)
    grad=lambda x,y:-np.array([np.cos(x*y)*y+2*x*mu,np.cos(x*y)*x + 2*x*mu])
    iterations_x, iterations_y=gradient_descent(func,grad,initial_point)
    sc=ax.scatter(iterations_x[-1],iterations_y[-1],alpha=0.4,
               c=mu, vmin=mu_min,vmax=mu_max)
ax.scatter(initial_point[0],initial_point[1],
           label='Ponto inicial',color='orange')
theta = np.linspace( 0 , 2 * np.pi , 150 )
radius = 1
a = radius * np.cos( theta )
b = radius * np.sin( theta )
ax.plot(a,b,color='green')
ax.legend(loc='upper center')
ax.set_aspect('equal')
fig.colorbar(sc)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.grid(True)
fig.savefig('teste.png')
