#! env/bin/python
import os
import glob
import shutil
import xmltodict
import zipfile
import json
import sys
import psycopg2
from stand_estimation_oopt.insertStandEstimation import insert_stand_estimation_oopt
from stand_estimation_leshoz.insertStandEstimation import insert_stand_estimation_leshoz
# from stand_estimation_oopt.fore
# from control_table import path, lezhoz_path, oopt_path, inv_path, geodata_rent_path, path_to_remove, path_to_copy

# path = "/home/r89/_projects/forest_python/incoming/*.collect-data"

cr_dbname = os.environ['DBNAME']
cr_user = os.environ['USER']
cr_password = os.environ['PASSWORD']
cr_host = os.environ['HOST']
incoming = os.getcwd() + '/incoming/'
json_folder = os.getcwd() + '/json/'
for filename in os.listdir('incoming'):
    if 'oopt' in filename:
        newFilename = filename
        zf = zipfile.ZipFile(incoming + filename, 'r')
        jsonNumber = 1
        for name in zf.namelist():
            if name.endswith('/'):
                continue
            if 'data/' in name:
                f = zf.open(name).read()
                newDict = xmltodict.parse(f, force_list={'forest_composition', 'forest_use_type', 'planned_forest_use_type',
                                                         'action_priority_1', 'tillage_1', 'creation_type_1', 'ecoproblems', 'plant_redflag', 'animal_redflag', 'main_plants'})

                with open(json_folder + filename+str(jsonNumber)+'.json', 'w') as outfile:
                    json.dump(newDict, outfile, indent=4)
                insert_stand_estimation_oopt(newDict)
                jsonNumber = jsonNumber+1
    elif 'leshoz' in filename:
        newFilename = filename
        zf = zipfile.ZipFile(incoming + filename, 'r')
        jsonNumber = 1
        for name in zf.namelist():
            if name.endswith('/'):
                continue
            if 'data/' in name:
                f = zf.open(name).read()
                newDict = xmltodict.parse(f, force_list={'forest_composition','forest_use_type','planned_forest_use_type','action_priority_1', 'tillage_1', 'creation_type_1', 'action_priority_2', 'action_priority_2', 'tillage_2', 'creation_type_2', 'planned_forest_composition'})
                with open(filename+str(jsonNumber)+'.json', 'w') as outfile:
                    json.dump(newDict, outfile, indent=4)
                insert_stand_estimation(newDict)
                jsonNumber = jsonNumber+1
    os.remove(filename)
# for filename in glob.glob(path):
#     print(path)
#     if 'rent_data' in filename:
#         # sub.call(geodata_rent_path, path)
#         print('initially I was like', path)
#         os.system(geodata_rent_path + ' {}'.format(path))
#     elif 'leshoz' in filename:
#         print(lezhoz_path)
#         os.system(lezhoz_path + ' {}'.format(path))
#     elif 'oopt' in filename:
#         print(oopt_path)

#         os.system(oopt_path + ' {}'.format(path))
#     elif 'inventory' in filename:
#         print('inv ', inv_path)
#         os.system(inv_path + ' {}'.format(path))

# for file in glob.glob(path_to_remove):
#     shutil.copy(file, path_to_copy)
#     os.remove(file)
