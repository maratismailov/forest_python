#!/usr/bin/python

import zipfile
import os
import xmltodict
import json
import glob
import psycopg2
import shutil
from insertGeometry import make_polygon
from insertRent import insert_rent
from credentials import cr_dbname, cr_host, cr_password, cr_user
import sys

# path = str(sys.argv[1])
path = "/home/r89/_projects/forest_python/incoming/*.collect-data"
# path = "/home/caiag/script/incoming/*.collect-data"


print('And then...', path)
def insertGeodata(path):
    path2 = "/home/r89/_projects/forest_python/geodata_collecting/incoming/*.collect-data"
    for filename in glob.glob(path):
        if 'rent_data' in filename:
            zf = zipfile.ZipFile(filename, 'r')
            jsonNumber = 1
            for name in zf.namelist():
                if name.endswith('/'):
                    continue
                if 'data/' in name:
                    f = zf.open(name).read()
                    # print(f)
                    newDict = xmltodict.parse(f,force_list={'rent_stand','rent_forest_use','rent_block','rent_coordinates'})
                    # d = xmltodict.parse(s, force_list={'car'})

                    # insert_stand_estimation(newDict)
                    # make_polygon(newDict)
                    insert_rent(newDict)
                    print('this is ahter q')


                    with open(filename+str(jsonNumber)+'.json', 'w') as outfile:
                        json.dump(newDict, outfile, indent=4)
                    # jsonData=json.dumps(newJson)
                    # dictData=json.loads(jsonData)
                    jsonNumber = jsonNumber+1
        else: continue

insertGeodata(path)