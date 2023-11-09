import pandas as pd
import routingpy as rp
import numpy as np
df=pd.read_csv('campus_usp.csv')
coordinates = df[['Longitude', 'Latitude']].values
api_key ='fee79717-7f76-483d-8fad-e338a180a4a8'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
durations = np.matrix(matrix.durations)
np.savetxt('matriz_campus.txt',durations)