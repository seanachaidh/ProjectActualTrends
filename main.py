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