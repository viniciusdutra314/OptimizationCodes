import cartopy.crs as ccrs
import matplotlib.pyplot as plt
plateCr = ccrs.PlateCarree()
plateCr._threshold = plateCr._threshold/1000.
ax = plt.axes(projection=plateCr)
ax.stock_img()

ny_lon, ny_lat = -50, -20
delhi_lon, delhi_lat = 77.23,78.61

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=1, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=plateCr,
         )

plt.savefig('geodesica.jpg',dpi=400)