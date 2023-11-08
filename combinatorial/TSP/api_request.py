import pandas as pd
df=pd.read_csv('gb_cities.csv')
coordinates = df[['Longitude', 'Latitude']].values
names = df['Place Name'].values
import routingpy as rp
import numpy as np

api_key ='ee28e2b6-a9e0-4f09-86ef-77a82b80877f'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
durations = np.matrix(matrix.durations)