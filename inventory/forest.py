#!/usr/bin/python
import zipfile
import os
import xmltodict
import json
import glob
import psycopg2
import shutil
import collections
# from insertGeometry import insert_coordinates
from insertInventory import insert_inventory
from credentials import cr_dbname, cr_host, cr_password, cr_user
# from insertAction1 import insert_action1
# from insertAction2 import insert_action2
# from insertStandEstimation import newId

# path = "/home/r89/_projects/forest_python/incoming/*.collect-data"
path = "/home/caiag/script/incoming/*.collect-data"
for filename in glob.glob(path):
    if 'inventory' in filename:
        newFilename = filename
        zf = zipfile.ZipFile(filename, 'r')
        jsonNumber = 1
        for name in zf.namelist():
            if name.endswith('/'):
                continue
            if 'data/' in name:
                f = zf.open(name).read() 
                newDict = xmltodict.parse(f)
            
                with open(filename+str(jsonNumber)+'.json', 'w') as outfile:
                    json.dump(newDict, outfile, indent=4)
                
                insert_inventory(newDict)
                # print(newDict)
                jsonNumber = jsonNumber+1
    else: continue