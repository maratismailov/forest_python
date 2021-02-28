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
from insertStandEstimation import insert_stand_estimation
from credentials import cr_dbname, cr_host, cr_password, cr_user
# from insertAction1 import insert_action1
# from insertAction2 import insert_action2
# from insertStandEstimation import newId

path = "/home/r89/_projects/forest_python/incoming/*.collect-data"
for filename in glob.glob(path):
    newFilename = filename
    zf = zipfile.ZipFile(filename, 'r')
    jsonNumber = 1
    for name in zf.namelist():
        if name.endswith('/'):
            continue
        if 'data/' in name:
            f = zf.open(name).read() 
            # print(f)
            newDict = xmltodict.parse(f)
            # print(newDict)
            # def fillWithValues(d):
            #     # print(d.items())
            #     for k, v in d.items():
            #         if isinstance(v, OrderedDict):
            #             fillWithValues(v)
            #         elif (d[k] is None):
            #             # d[k] = 'null'
            #             print('ele is none ', d[k])
            #         else:
            #             continue

            # fillWithValues(newDict)
            # print(newDict)
            with open(filename+str(jsonNumber)+'.json', 'w') as outfile:
                json.dump(newDict, outfile, indent=4)
            
            insert_stand_estimation(newDict)
            testData = (
                None,
                None
            )
           
            
            # jsonData=json.dumps(newJson)
            # dictData=json.loads(jsonData)
            jsonNumber = jsonNumber+1
            # print(newDict['stand_estimation']['old_stands']['value'])