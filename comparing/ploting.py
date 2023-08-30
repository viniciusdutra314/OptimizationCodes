import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df_newton=pd.read_csv("temporario/newton.csv")
df_halley=pd.read_csv("temporario/halley.csv")
quantidade=16
newton_medias=[1e-9*sum(df_newton['Tempo'][1000*i:1000*(i+1)]) for i in range(quantidade)]
halley_medias=[1e-9*sum(df_halley['Tempo'][1000*i:1000*(i+1)]) for i in range(quantidade)]
halley_newton=[halley_medias[j]/newton_medias[j] for j in range(quantidade)]
fig,axes=plt.subplots()
axes.scatter(range(quantidade),newton_medias,label='Newton')
axes.scatter(range(quantidade),halley_medias,label="Halley")
axes.set_xlabel(r"$log(\epsilon)$")
axes.set_ylabel(r"Tempo de processamento (s)")
print(sum(df_newton['Tempo']))
print(sum(df_halley['Tempo']))
axes.grid()
axes.legend()
fig.savefig("temporario//exemplo.png",dpi=400)