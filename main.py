import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely import geometry
import seaborn as sns

try:
    import pycpt
    cmap = pycpt.load.cmap_from_cptcity_url('ukmo/wow/temp-c.cpt')
except:
    cmap = 'Spectral_r'

mag_data = pd.read_csv('./data/processed/mag.csv', index_col=0)
mag_data['geometry'] = [geometry.Point(x, y) for x, y in zip(mag_data['long_wgs84'], mag_data['lat_wgs84'])]
mag_data = gpd.GeoDataFrame(mag_data, geometry='geometry', crs="+init=epsg:4326")

mag_data.head()