import matplotlib.pyplot as plt
import subprocess
from os import getcwd
import numpy as np
x=np.linspace(0,10,100)
y=[]
for j in x:
    command=[getcwd()+"/./newton1d",str(j)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    y.append(float(result.stdout))
plt.plot(x,y)
plt.xlabel(r"Chute inicial $x_0$")
plt.ylabel(r"Valor convergente")
plt.title(r"$sin(x)$ pelo método de Newton")
plt.ylim(0,20)
multiplos=[np.pi*i for i in range(4)]
for j in multiplos:
    plt.axhline(y=j, color='r', linestyle='--',alpha=0.5)
plt.savefig("teste.png")