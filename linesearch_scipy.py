import scipy.optimize as sci
import matplotlib.pyplot as plt
def obj_func(x): return x**4+x**3 -5*x**2 +11*x -10
def obj_grad(x): return 4*x**3 +3*(x**2) -(10)*x +11

point = 11 #starting point
x_values=[point]
while True:
    direction=-obj_grad(point) 
    result=sci.line_search(obj_func, obj_grad, point, direction)
    alpha=result[0]
    try: #quando estiver muito próximo da raiz, a precisão finita dos float
        #causará uma except, então podemos parar o algoritmo
        point+=alpha*direction
        x_values.append(point)
    except: break

print(f"no ponto {point} a derivada é {obj_grad(point)}")
plt.scatter(range(len(x_values)), x_values)
plt.xlabel("Interações (k)")
plt.ylabel(r"$f(x_k)$")
plt.title(r"Line search $y=x^4+x^3-5x^2+11x-10$")
plt.axhline(point,color="red",alpha=0.5,label="Raiz")
plt.legend()
plt.savefig("Line_search")