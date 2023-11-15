from receive_args_view import get_args
import matplotlib.pyplot as plt
shortestpath,coords, data, start, end = get_args()
x_value=[x for x in coords['x_value']]
y_value=[y for y in coords['y_value']]
plt.scatter(x_value,y_value,label='Pontos',color='r')
x_value=[coords.iloc[int(i)][1] for i in shortestpath[1]]
y_value=[coords.iloc[int(i)][2] for i in shortestpath[1]]
plt.plot(x_value,y_value,label='Caminho encontrado')
plt.grid()
plt.legend()
plt.title(f"fitness = {shortestpath[0]}")
plt.savefig('temp.jpg')