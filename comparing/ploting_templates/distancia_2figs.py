import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df_newton=pd.read_csv("temporario/newton.csv")
df_halley=pd.read_csv("temporario/halley.csv")
newton_medias=[1e-9*sum(df_newton['Tempo'][1000*i:1000*(i+1)]) for i in range(50)]
halley_medias=[1e-9*sum(df_halley['Tempo'][1000*i:1000*(i+1)]) for i in range(50)]
halley_newton=[halley_medias[j]/newton_medias[j] for j in range(50)]
fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[1].scatter(range(50),newton_medias,label='Newton')
axes[1].scatter(range(50),halley_medias,label="Halley")
axes[1].set_xlabel("Amplitude do x0 inicial")
axes[1].set_ylabel(r"Tempo de processamento (s)")
axes[1].set_title("Polinômio de 3 ºGrau com raizes distintas")
print(sum(df_newton['Tempo']))
print(sum(df_halley['Tempo']))
axes[1].grid()
axes[1].legend()
axes[0].scatter(range(len(halley_newton)),halley_newton,color='g',label="Halley/Newton")
axes[0].set_xlabel("Amplitude do x0 inicial")
axes[0].set_ylabel("Razão Halley/Newton")
axes[0].legend()
axes[0].grid()
fig.savefig("temporario//exemplo.png",dpi=400)