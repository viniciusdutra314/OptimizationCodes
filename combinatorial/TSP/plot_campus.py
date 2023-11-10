import argparse

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

distances=np.loadtxt('dados//matriz_campus.txt')
coordinates=pd.read_csv('dados//campus_usp.csv')


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
for j in range(N-1):
    arrow_start = (x[j], y[j])  
    arrow_end = (x[j+1], y[j+1])    
    arrow_properties = dict(facecolor='green', edgecolor='green', 
                            arrowstyle='->',linestyle='--')
    ax.annotate('', xytext=arrow_start, xy=arrow_end, 
                arrowprops=arrow_properties,
                ha='center', va='center')
for index, row in coordinates.iterrows():
    ax.text(row['Longitude'], row['Latitude'], 
            row['Campus'],fontsize=8,color='blue', 
            transform=ccrs.PlateCarree(), )
ax.scatter(coordinates['Longitude'],coordinates['Latitude'],
           color='r',label='Campi USP')
if permutation[0]!=permutation[-1]:
    ax.scatter(x[0],y[0],label='Início',color='purple')
    ax.scatter(x[-1],y[-1],label='Fim',color='aqua')
else:
    ax.scatter(x[0],y[0],label='Começo do ciclo',color='purple')
ax.set_title(f"Distância total de {total_value}km")
ax.legend()
ax.axis('equal')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.STATES)
fig.savefig('temp_resultado.jpg',dpi=400)