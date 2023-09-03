import pandas as pd
import numpy as np
arquivos=["dados/halley_2grau_distintas.csv","dados/halley_3grau_ate100.csv","dados/halley_3grau_distintas.csv",
          "dados/halley_3grau_erro50.csv","dados/halley_4grau_distintas.csv","dados/halley_grau100_erro50.csv",
          "dados/halley_grau100.csv"]
for j in arquivos:
    df_halley=pd.read_csv(j)
    df_newton=pd.read_csv(j.replace("halley","newton"))
    resultado=df_halley['Iterações']>=100
    resultado_newton=df_newton['Iterações']>=100
    print(np.sum(resultado)/len(resultado), np.sum(resultado_newton)/len(resultado_newton))