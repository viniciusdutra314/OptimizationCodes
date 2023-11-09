import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs ; import cartopy.feature as cfeature
durations=np.loadtxt('matriz_campus.txt')
coordinates=pd.read_csv('campus_usp.csv')


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.STATES)
ax.scatter(coordinates['Longitude'],coordinates['Latitude'],
           color='r',label='Campus USP')
for index, row in coordinates.iterrows():
    ax.text(row['Longitude'], row['Latitude'], 
            row['Campus'], transform=ccrs.PlateCarree(), 
            fontsize=8, color='blue')
best_permutation=(6, 0, 1, 3, 4, 7, 2, 5)
x=[coordinates['Longitude'][j] for j in best_permutation]
y=[coordinates['Latitude'][j] for j in best_permutation]
ax.plot(x,y,label='Caminho ótimo',linestyle='dashed')
ax.legend()
ax.axis('equal')

fig.savefig('mapa_saopaulo_caminho_minimo.jpg',dpi=400)