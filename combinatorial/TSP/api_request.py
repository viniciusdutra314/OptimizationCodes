import numpy as np
import pandas as pd
import routingpy as rp

df = pd.read_csv('dados//campus_usp.csv')
coordinates = df[['Longitude', 'Latitude']].values
api_key = '01ebf754-830b-493d-aa76-e6e1b540d5e9'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
distances = np.matrix(matrix.distances)
distances = np.round(distances/1000)
np.savetxt('dados//matriz_campus.txt', distances)
