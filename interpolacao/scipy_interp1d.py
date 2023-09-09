import scipy.interpolate as sci
import matplotlib.pyplot as plt
import numpy as np

N = 10
x_data = np.linspace(0, 1, N)
y_data = np.random.uniform(size=N)
kinds = ["nearest", "nearest-up", "zero", "slinear",
         "linear", "quadratic", "cubic"]

figure, axis = plt.subplots(ncols=4, nrows=2, figsize=(20, 10))

for index, kind in enumerate(kinds):
    row = index // 4  
    col = index % 4   
    interpolacao = sci.interp1d(x_data, y_data, kind=kind)
    t = np.linspace(0, 1, 1000)
    axis[row, col].scatter(x_data, y_data)
    axis[row, col].plot(t, interpolacao(t))
    axis[row, col].set_title(f'{kind}')
    axis[row,col].grid()

figure.tight_layout()  
figure.savefig('scipy.png')
