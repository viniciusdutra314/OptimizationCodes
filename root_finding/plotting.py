import matplotlib.pyplot as plt
import numpy as np
with open("data_bisnewton.dat","r") as txt:
    linhas=txt.readlines()
    x=np.array([int(j.replace("\n","").split()[0]) for j in linhas])
    y=np.array([abs(np.float64(j.replace("\n","").split()[1])) for j in linhas])
print(x,y)
print(x,np.log10(y))
plt.plot(x,np.log10(y))
plt.xlabel("Número de Iterações")
plt.ylabel("Valor absoluto da função (log)")
plt.savefig("newton-bissec.png")