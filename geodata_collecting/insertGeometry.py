import psycopg2
from shapely.geometry import MultiPolygon, Polygon
import zipfile
import xmltodict
import shutil
import glob
from credentials import cr_dbname, cr_host, cr_password, cr_user


def make_polygon(coordinates, plot_name, forest_use_type, block_str, stand_str_global, rent_id, leshoz_id):

    lon_list = []
    lat_list = []
    for coordinate in coordinates:
        print(coordinate)
        lonElement = coordinate['coordinates']['x']
        latElement = coordinate['coordinates']['y']
        lon_list.append(float(lonElement))
        lat_list.append(float(latElement))
    polygon_geom = Polygon(zip(lon_list, lat_list))
    insert_coordinates(polygon_geom, plot_name, forest_use_type,
                       block_str, stand_str_global, rent_id, leshoz_id)
    return polygon_geom


def insert_coordinates(polygon_geom, plot_name, forest_use_type, block_str, stand_str_global, rent_id, leshoz_id):
    """ insert values into the rentuse table """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        coordinate_query = """INSERT INTO rent.rentuse (
        rent_id,
        forestusetype_id,
        leshoz_id,
        standlist,
        leaselot_name,
        block_ids,
        geom
        )
        VALUES({}, {}, {}, '{}', '{}', '{}', ST_SETSRID(ST_Multi(ST_GeomFromText('{}', 4326)),0))
        """.format(rent_id, forest_use_type, leshoz_id, stand_str_global, plot_name, block_str, polygon_geom)
        cur.execute(coordinate_query)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
