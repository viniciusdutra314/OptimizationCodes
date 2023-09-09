import numpy as np
import matplotlib.pyplot as plt
x_data,y_data=np.random.uniform(size=(2,10))
def interpolacao_linear(x_data:float,y_data:float) -> callable:
    def funcao(x):
        global x_data,y_data
        #precisamos ordenar nossos dados
        dicionario={x_data[i]:y_data[i] for i in range(len(x_data))}
        organizado = sorted(dicionario.items())
        x_data, y_data = zip(*organizado)
        for i in range(len(x_data)-1):
            if x_data[i]<= x <x_data[i+1]:
                delta_y=y_data[i+1]-y_data[i]
                delta_x=x_data[i+1]-x_data[i]
                return y_data[i]+(x-x_data[i])*delta_y/delta_x
    return np.vectorize(funcao)
interpolacao=interpolacao_linear(x_data,y_data)
t=np.linspace(0,9,10000)
plt.scatter(x_data,y_data,label='Dados')
plt.plot(t,interpolacao(t),label='interpolação linear')
plt.savefig('interpolacao_linear.png')