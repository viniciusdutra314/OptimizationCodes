import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
quantidade=50
filename='distancia_2grau'
df_newton=pd.read_csv(f"newton_{filename}.csv")
df_halley=pd.read_csv(f"halley_{filename}.csv")
filter_newton=df_newton['Convergiu']==1
filter_halley=df_halley['Convergiu']==1
df_newton=df_newton[filter_newton]
df_halley=df_halley[filter_halley]
newton_medias=np.array([1e-9*df_newton.loc[df_newton['Distancia']==i, 'Tempo'].sum() for i in range(quantidade)])
halley_medias=np.array([1e-9*df_halley.loc[df_halley['Distancia']==i, 'Tempo'].sum() for i in range(quantidade)])
halley_newton=halley_medias/newton_medias
fig,axes=plt.subplots(1,2,figsize=(10,6))
axes[1].scatter(range(quantidade),newton_medias,label='Newton')
axes[1].scatter(range(quantidade),halley_medias,label="Halley")
axes[1].set_xlabel("Amplitude de x0")
axes[1].set_ylabel("Tempo de processamento (s)")
print(sum(df_newton['Tempo']))
print(sum(df_halley['Tempo']))
axes[1].grid()
axes[1].legend()
axes[0].scatter(range(quantidade),halley_newton,color='g')
axes[0].set_xlabel("Amplitude de x0")
axes[0].set_ylabel("Razão Halley/Newton")
axes[0].axhline(np.mean(halley_newton),label=f"Média = {round(np.mean(halley_newton),2)}")
axes[0].grid()
axes[0].legend()
fig.suptitle("Polinômio de 2ºgrau")
fig.savefig(f"{filename}.png",dpi=400)