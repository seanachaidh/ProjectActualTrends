import pandas as pd
from scipy import spatial
from util import to_Cartesian,geo_to_cartesian,distToKM,kmToDIST
import geopandas as gpd
import numpy as np
from geopandas.tools import sjoin
import folium
from folium.plugins import MarkerCluster
import shapely
from shapely.geometry import Point
import unicodedata
import pysal as ps
from shapely import geometry
import sys
from folium import plugins
import string
import folium
from shapely import wkt, geometry
import json
from pprint import pprint
from openrouteservice import client, places
from openrouteservice import distance_matrix
from geopandas import GeoDataFrame
from shapely.geometry import Point
import osrm
from openrouteservice import geocoding

import re


#import osrm
#reload(sys)
#sys.setdefaultencoding('utf-8')

#Setup open-route service client
api_key = '58d904a497c67e00015b45fc07893889d08b4b6abcfc82938c195ec0'
clnt = client.Client(key=api_key)


# Make a new RequestConfig object
MyConfig = osrm.RequestConfig()
MyConfig.host = "http://router.project-osrm.org"  # Only change the host
osrm.RequestConfig.host = "router.project-osrm.org"
osrm.RequestConfig.host

#Read data
column_names = 'id;'.split(";")

all_data = pd.read_csv('./data/processed_data.csv',sep=",")

#Convert geo-coordinates to cartesian
all_data['x'], all_data['y'], all_data['z'] = geo_to_cartesian(all_data['long_wgs84'],all_data['lat_wgs84'])

stationArr = all_data[['lat_wgs84', 'long_wgs84']].as_matrix()

import geocoder

#https://geopy.readthedocs.io/en/stable/
from geopy.geocoders import Nominatim

addresses=[]
#Reverse geo code the address name
for i in range(len(all_data)):
    x = all_data['lat_wgs84'][i]
    y = all_data['long_wgs84'][i]
    #geolocator = Nominatim()
    #location = geolocator.reverse([x, y])
    address = all_data['address'][i]
    name = address.split('-')
    addresses.append(name[0].capitalize())
    #g = geocoder.google([y,x], method='reverse')
    #print(g.street)
    #all_data['name'] = clnt.reverse_geocode(location=(x, y))['features'][0]['properties']['name']
    
all_data['name'] = addresses
all_data.to_csv('./data/final_dataset.csv')
#locationlist = zip(all_data['long_wgs84'],all_data['lat_wgs84'])
locationlist = [[all_data['long_wgs84'][i],all_data['lat_wgs84'][i]] for i in range(len(all_data)) ]