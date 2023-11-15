import numpy as np
import pandas as pd
import routingpy as rp
arquivo='us_states'
df = pd.read_csv(f'coord_{arquivo}.csv')
coordinates = df[['Longitude', 'Latitude']].values
api_key = '28fe8a83-dce1-4de0-b8d0-1886b440a874'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
distances = np.matrix(matrix.distances)
distances = np.round(distances/1000)
np.savetxt(f'matriz_{arquivo}.txt', distances)
