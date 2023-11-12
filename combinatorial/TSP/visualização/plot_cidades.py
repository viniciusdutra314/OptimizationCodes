
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import routingpy as rp

from receive_args_view import get_args
shortestpath,coords,data,start,end=get_args()
total_value,permutation=shortestpath
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

N=len(permutation)
x=[coords['Longitude'][j] for j in permutation]
y=[coords['Latitude'][j] for j in permutation]

api_key = '4997bc4c-ec02-44c2-a873-310553d2f25f'
api = rp.Graphhopper(api_key=api_key)

for i in range(N-1):
    path=api.directions(locations=[(x[i],y[i]),
                                   (x[i+1],y[i+1])],profile='car')
    x_path=[j[0] for j in path.geometry]
    y_path=[j[1] for j in path.geometry]
    path_label=None if i!=0 else 'Caminhos ótimos'
    ax.plot(x_path,y_path,color='lime',
            linestyle='dashed',alpha=0.7,label=path_label)
ax.set_title(f"Distância total de {total_value}km")

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.STATES)

ax.scatter(coords['Longitude'],coords['Latitude'],
           color='r',label='Cidades')
if permutation[0]!=permutation[-1]:
    ax.scatter(x[0],y[0],label='Início',color='purple')
    ax.scatter(x[-1],y[-1],label='Fim',color='aqua')
else:
    ax.scatter(x[0],y[0],label='Começo do ciclo',color='purple')

dy=np.max(coords['Latitude'])-np.min(coords['Latitude'])

for index in range(len(permutation)):
        num=permutation[index]
        text_to_box=f"({index}){coords['Cidade'][num]}"
        x_coord=coords['Longitude'][num]
        y_coord=coords['Latitude'][num]
        ax.text(x_coord, y_coord-0.04*dy, 
                text_to_box,fontsize=4,color='blue', 
                transform=ccrs.PlateCarree(), 
                backgroundcolor='white')

ax.legend()
ax.axis('equal')
fig.savefig('temp_resultado.jpg',dpi=400)