import psycopg2
from shapely.geometry import MultiPolygon, Polygon
import zipfile
# import os
# import xmltodict
import shutil
import glob
from credentials import cr_dbname, cr_host, cr_password, cr_user
# from forest import newDict

# path = "/home/r89/_projects/forest_python/incoming/*.collect-data"
# for filename in glob.glob(path):
#     newFilename = filename
#     zf = zipfile.ZipFile(filename, 'r')
#     jsonNumber = 1
#     for name in zf.namelist():
#         if name.endswith('/'): continue
#         if 'data/' in name:
#             f = zf.open(name).read()
#             newDict = xmltodict.parse(f)




def insert_polygon(newDict, newId, forestry_num, block_id):
    print('almost')

    leshoz_num = newDict['stand_estimation']['oopt']['code']
    forestry_num = newDict['stand_estimation']['zone']['code']
    block_num = newDict['stand_estimation']['block']['value']
    stand_num = newDict['stand_estimation']['stand_code']['value']
    cycle = newDict['stand_estimation']['cycle']['value']
    lon_list = []
    lat_list = []
    # print(newDict['stand_estimation']['stand_coordinates'])
    if len(newDict['stand_estimation']['stand_coordinates']) > 1:
        for coordinate in newDict['stand_estimation']['stand_coordinates']:
            # print(coordinate)
            lonElement = coordinate['stand_coordinates']['x']
            latElement = coordinate['stand_coordinates']['y']
            lon_list.append(float(lonElement))
            lat_list.append(float(latElement))
    else:
        coordinate = newDict['stand_estimation']['stand_coordinates']
        print('ddd', coordinate)
        lonElement = coordinate['stand_coordinates']['x']
        latElement = coordinate['stand_coordinates']['y']
        lon_list.append(float(lonElement))
        lat_list.append(float(latElement))
    polygon_geom = Polygon(zip(lon_list, lat_list))

    insert_coordinates(polygon_geom, newId, leshoz_num, forestry_num, block_num, block_id, stand_num, cycle)
    return polygon_geom


def insert_coordinates(polygon_geom, stand_code_str, leshoz_num, forestry_num, block_num, block_id, stand_num, cycle):
    """ delete values from the stand table"""
    delete_geometry_query = """DELETE FROM forest.stand WHERE stand_code = {} AND cycle = {}""".format(stand_code_str, cycle)
    """ insert a values into the stand table """
    coordinate_query = """INSERT INTO forest.stand (
        the_geom,
        stand_code,
        leshoz_num,
        forestry_num,
        block_num,
        stand_num,
        block_id,
        cycle
        )
        VALUES(ST_SETSRID(ST_Multi(ST_GeomFromText('{}', 4326)),0), {}, {}, {}, {}, {}, {}, {})
        """.format(polygon_geom, stand_code_str, leshoz_num, forestry_num, block_num, stand_num, block_id, cycle)

    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(delete_geometry_query)
        cur.execute(coordinate_query)
        print('stand cycle is ', cycle)
     
        conn.commit()
        cur.close()
        print('geometry', stand_code_str)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# insert_coordinates()
