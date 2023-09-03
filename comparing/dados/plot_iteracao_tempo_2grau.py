import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
quantidade=50
filename='iteracao_tempo_2grau'
df_newton=pd.read_csv(f"newton_{filename}.csv")
df_halley=pd.read_csv(f"halley_{filename}.csv")
filter_newton=df_newton['Convergiu']==0
filter_halley=df_halley['Convergiu']==0
df_newton=df_newton[~filter_newton]
df_halley=df_halley[~filter_halley]
halley_newton=df_halley['Iterações']/df_newton['Iterações']
fig,axes=plt.subplots(1,2,figsize=(10,6))
axes[1].scatter(df_newton['Iterações'],1e-6*df_newton['Tempo'],label='Newton')
axes[1].scatter(df_halley['Iterações'],1e-6*df_halley['Tempo'],label="Halley")
axes[1].set_xlabel("Iterações")
axes[1].set_ylabel(r"Tempo de processamento ($\mu$ s)")
print(sum(df_newton['Tempo']))
print(sum(df_halley['Tempo']))
axes[1].grid()
axes[1].legend()
axes[0].hist(halley_newton,bins=100)
axes[0].set_xlabel("Razão Iterações Halley/Newton")
axes[0].set_ylabel("Histograma")
axes[0].set_xlim(0,1.5)
axes[0].grid()
axes[0].legend()
fig.suptitle("Polinômio aleatório de 2º grau")
fig.savefig(f"{filename}.png",dpi=400)