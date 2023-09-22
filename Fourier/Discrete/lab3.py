import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
link='https://raw.githubusercontent.com/viniciusdutra314/CanalSingularidade/main/GraficosCientificos/osciloscopio.csv'
dataframe=pd.read_csv(link,decimal=',')
#No brasil usamos a virgula ao invés de ponto (exemplo: 0,5 e não 0.5)
#Isso geralmente faz com que o pandas importe os dados como texto e não como numeros
fig, axis=plt.subplots()
print(dataframe)
tempo=[float(j.replace(",",".")) for j in dataframe["Time"]]
voltagem=[float(j.replace(",",".")) for j in dataframe["Volt"]]
axis.scatter(tempo,voltagem,s=5.5)
fig.savefig("teste.png")