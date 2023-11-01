import numpy as np
import matplotlib.pyplot as plt
import pulp as lp

N = 10
degree=2
x = np.linspace(1, 10, N)
y = (x**2)*(1 + 0.05* np.random.normal(size=N)) -7* x * (1 + 0.05* np.random.normal(size=N))+4
y[3]=30
problem = lp.LpProblem("LinearProgrammingExample", lp.LpMinimize)
coefs=[lp.LpVariable(f'a{i}') for i in range (degree+1)]
variables=[lp.LpVariable(f"x{i}") for i in range(N)]
objective = lp.lpSum(variables)
problem += objective
for j in range(2):
    sign = (-1) ** (j+1)
    for i in range(N):
        polynominal_error=sum([coefs[j]*(x[i]**j) for j in range(degree+1)])-y[i]
        problem += variables[i]>=sign*polynominal_error
problem.solve()
print("Status:", lp.LpStatus[problem.status])
print("Optimal Solution:")
for variable in variables:
    print(f"{variable.name}: {variable.varValue}")
coefs=[coef.varValue for coef in coefs]
coefs_quadraticos=np.polyfit(x,y,degree)[::-1]
print(coefs)
print(coefs_quadraticos)
polinomio=np.vectorize(lambda x: sum(coefs[i]*x**i for i in range(degree+1)))
polinomio_quadratico=np.vectorize(lambda x: sum(coefs_quadraticos[i]*x**i for i in range(degree+1)))
plt.scatter(x, y, label="Data")
plt.plot(x:=np.linspace(0,10,100),polinomio(x),color='r',label='Erro absoluto')
plt.plot(x:=np.linspace(0,10,100),polinomio_quadratico(x),color='g',label='Erro Quadrático')
plt.legend()
plt.grid()
plt.savefig('outsider_parabola.jpg')
