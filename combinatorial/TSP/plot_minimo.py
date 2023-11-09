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
    ax.text(row['Longitude']*(1.4), row['Latitude']*(1+4), 
            row['Campus'], transform=ccrs.PlateCarree(), 
            fontsize=8, color='blue')
    

    
ax.legend()
ax.axis('equal')

fig.savefig('mapa_saopaulo_caminho_minimo.jpg',dpi=400)