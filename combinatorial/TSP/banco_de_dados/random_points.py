import numpy as np
import pandas as pd
num_points=100
coordinates=np.random.random(size=(num_points,2))
data=np.zeros((num_points,num_points))
for i in range(num_points):
    for j in range(num_points):
        data[i][j]=np.linalg.norm(coordinates[i]-coordinates[j])
np.savetxt('banco_de_dados//matriz_random.txt',data)
df=pd.DataFrame(coordinates,columns=['x_value','y_value'])
df.to_csv('banco_de_dados//coord_random.csv')