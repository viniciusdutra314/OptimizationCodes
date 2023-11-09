import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs ; import cartopy.feature as cfeature
durations=np.loadtxt('duracoes.txt')
coordinates=pd.read_csv('gb_cities.csv')
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_local_search
permutation,distance=solve_tsp_local_search(durations)
print(permutation,distance)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.scatter(coordinates['Longitude'],coordinates['Latitude'],
           color='r',label='Cidades')
ax.legend()
ax.axis('equal')
fig.savefig('UK.jpg',dpi=400)