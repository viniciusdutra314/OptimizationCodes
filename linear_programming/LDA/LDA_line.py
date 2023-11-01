import numpy as np
import matplotlib.pyplot as plt
import pulp as lp

N = 10
x = np.linspace(1, 10, N)
y = -7* x * (1 + 0.1* np.random.normal(size=N))


problem = lp.LpProblem("LinearProgrammingExample", lp.LpMinimize)
a,b=lp.LpVariable('a'),lp.LpVariable('b')
variables=[lp.LpVariable(f"x{i}") for i in range(N)]
objective = lp.lpSum(variables)
problem += objective
for j in range(2):
    sign = (-1) ** (j+1)
    for i in range(N):
        problem += variables[i]>=sign*(a*x[i]+b+-y[i])
problem.solve()
print("Status:", lp.LpStatus[problem.status])
print("Optimal Solution:")
for variable in variables:
    print(f"{variable.name}: {variable.varValue}")
a=a.varValue
b=b.varValue
print(f"a={a} b={b}")
a_quadratico,b_quadratico=np.polyfit(x,y,1)
reta=np.vectorize(lambda x: a*x +b)
reta_quadratico=np.vectorize(lambda x:a_quadratico*x +b_quadratico)
plt.scatter(x, y, label="Data")
plt.plot(x:=np.linspace(0,10,100),reta(x),color='r',label='Erro absoluto')
plt.plot(x:=np.linspace(0,10,100),reta_quadratico(x),color='g',label='Erro Quadrático')
plt.legend()
plt.grid()
plt.savefig('outsider.jpg')
