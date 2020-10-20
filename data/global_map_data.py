import pandas as pd
import plotly.express as px

data = pd.read_excel('data/botucatu_radiation_latlong.xlsx')
df = pd.DataFrame(data)

df[['lat', 'lon']] = df['lat-long'].str.split(',', expand=True)

df['lat'] = df['lat'].astype(dtype='float64')
df['lon'] = df['lon'].astype(dtype='float64')
