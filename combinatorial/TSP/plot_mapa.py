import argparse
import os

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import routingpy as rp
diretorio=os.path.join(os.getcwd(),'run_folder')
arquivo=[file for file in os.listdir(diretorio) if file.endswith('.csv')]
assert len(arquivo)==1 , "Mais de uma base de dados selecionada na run_folder"
arquivo=os.path.splitext(arquivo[0])[0]


coordinates=pd.read_csv(f'run_folder//{arquivo}.csv')
distances=np.loadtxt(f'run_folder//matriz_{arquivo}.txt')

parser=argparse.ArgumentParser()
parser.add_argument("total_value",type=float)
parser.add_argument("permutation",nargs='+',type=int)
args=parser.parse_args()
total_value=args.total_value
permutation=args.permutation


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

N=len(permutation)
x=[coordinates['Longitude'][j] for j in permutation]
y=[coordinates['Latitude'][j] for j in permutation]

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

ax.scatter(coordinates['Longitude'],coordinates['Latitude'],
           color='r',label='Cidades')
if permutation[0]!=permutation[-1]:
    ax.scatter(x[0],y[0],label='Início',color='purple')
    ax.scatter(x[-1],y[-1],label='Fim',color='aqua')
else:
    ax.scatter(x[0],y[0],label='Começo do ciclo',color='purple')

dy=np.max(coordinates['Latitude'])-np.min(coordinates['Latitude'])

for index in range(len(permutation)-1):
        num=permutation[index]
        text_to_box=f"({index}){coordinates['Cidade'][num]}"
        x_coord=coordinates['Longitude'][num]
        y_coord=coordinates['Latitude'][num]
        ax.text(x_coord, y_coord-0.04*dy, 
                text_to_box,fontsize=4,color='blue', 
                transform=ccrs.PlateCarree(), 
                backgroundcolor='white')

ax.legend()
ax.axis('equal')
fig.savefig('temp_resultado.jpg',dpi=400)