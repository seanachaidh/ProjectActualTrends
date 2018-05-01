#Import the necessary Python moduless
import pandas as pd
import geopandas as gpd
import numpy as np
from geopandas.tools import sjoin
import folium
from folium.plugins import MarkerCluster
from folium.element import IFrame
import shapely
from shapely.geometry import Point
import unicodedata
import pysal as ps
from shapely import geometry
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Read data
column_names = 'id;'.split(";")

all_data = pd.read_csv('./data/processed_data.csv',sep=",")



locations = all_data[['latitude', 'longitude']]
locationlist = locations.values.tolist()
len(locationlist)
locationlist[7]

map2 = folium.Map(location=[0, -77.05], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=all_data['address'][point]).add_to(map)
map2


