import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
quantidade=50
filename='grau_variavel'
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
axes[1].scatter(range(0,quantidade,2),newton_medias[0::2],label='Newton par')
axes[1].scatter(range(0,quantidade,2),halley_medias[0::2],label="Halley par")
axes[1].scatter(range(1,quantidade,2),newton_medias[1::2],label='Newton impar')
axes[1].scatter(range(1,quantidade,2),halley_medias[1::2],label="Halley impar")
axes[1].set_xlabel("Grau do polinômio")
axes[1].set_ylabel("Tempo de processamento (s)")
axes[1].set_yscale('log')
print(sum(df_newton['Tempo']))
print(sum(df_halley['Tempo']))
axes[1].grid()
axes[1].legend()
axes[0].scatter(range(0,quantidade,2),halley_newton[0::2],label="par")
axes[0].scatter(range(1,quantidade,2),halley_newton[1::2],label="Impar")
axes[0].set_xlabel("Grau do polinômio")
axes[0].set_ylabel("Razão Halley/Newton")
axes[0].axhline(np.mean(halley_newton[3::]),label=f"Média = {round(np.mean(halley_newton[3::]),2)}")
axes[0].grid()
axes[0].legend()
fig.savefig(f"{filename}.png",dpi=400)