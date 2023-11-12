import numpy as np
import pandas as pd
import routingpy as rp
arquivo='usp'
df = pd.read_csv(f'coord_{arquivo}.csv')
coordinates = df[['Longitude', 'Latitude']].values
api_key = '4997bc4c-ec02-44c2-a873-310553d2f25f'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
distances = np.matrix(matrix.distances)
distances = np.round(distances/1000)
np.savetxt(f'matriz_{arquivo}.txt', distances)
