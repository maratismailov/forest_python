import zipfile
import os
import xmltodict
import json
import glob
import psycopg2
import shutil
# import geopandas as gpd
# from shapely.geometry import Polygon
from ppygis3 import Point, LineString, Geometry

lat_list = [50.854457, 52.518172, 50.072651, 48.853033, 50.854457]
lon_list = [4.377184, 13.407759, 14.435935, 2.349553, 4.377184]

path = "/home/r89/_projects/forest_python/incoming/*.collect-data"
for filename in glob.glob(path):
    newFilename = filename
    zf = zipfile.ZipFile(filename, 'r')
    jsonNumber = 1
    for name in zf.namelist():
        if name.endswith('/'): continue
        if 'data/' in name:
            f = zf.open(name).read()
            newDict = xmltodict.parse(f)
            # print(standCount, 'count')
            # insert_action(newDict)

# polygon_geom = Polygon(zip(lon_list, lat_list))
# crs = {'init': 'epsg:4326'}
# polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])   
polygon = LineString(Point(1.0, 2.0))
print(polygon)
           



