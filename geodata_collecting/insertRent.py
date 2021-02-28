import psycopg2
from shapely.geometry import MultiPolygon, Polygon
import zipfile
import xmltodict
import shutil
import glob
from credentials import cr_dbname, cr_host, cr_password, cr_user
from insertGeometry import make_polygon


def insert_rent(newDict):


    def get_block_id(forestry_id, block_num):
        get_block_id_query = """SELECT gid FROM forest.block WHERE forestry_id = {} AND block_num = {}""".format(forestry_id, block_num)
        insert_block_query ="""INSERT INTO forest.block (
        forestry_id,
        block_num
        )
        VALUES(%s, %s)
        RETURNING gid"""
        block_data = (
            forestry_id,
            block_num
        )
        conn = None
        try:
            conn = psycopg2.connect(
                dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
            cur = conn.cursor()
            cur.execute(get_block_id_query)
            is_block = cur.rowcount
            if is_block == 0:
                cur.execute(insert_block_query, block_data)
                block_id = cur.fetchone()[0]
            else:
                cur.execute(get_block_id_query)
                block_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return block_id

    # region = newDict['rent_geodata']['region']['code']
    leshoz = newDict['rent_geodata']['leshoz']['code']
    forestry = newDict['rent_geodata']['forestry']['code']
    contract_num = newDict['rent_geodata']['contract_number']['value']
    year = newDict['rent_geodata']['contract_date']['year']
    month = newDict['rent_geodata']['contract_date']['month']
    day = newDict['rent_geodata']['contract_date']['day']

    contract_date = year + '-' + month + '-' + day

    insert_into_rent_table_query = """INSERT INTO rent.rent (
        contract_num,
        contract_date,
        leshoz_id,
        forestry_id
        )
        VALUES(%s, %s, %s, %s)
        RETURNING rent_id"""
    contract_data = (
        contract_num,
        contract_date,
        leshoz,
        forestry
    )

    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(insert_into_rent_table_query, contract_data)
        rent_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


    for rent_forest_use in newDict['rent_geodata']['rent_forest_use']:
        plot_name = rent_forest_use['plot_name']['value']
        forest_use_type = rent_forest_use['forest_use_type']['code']
        coordinates = rent_forest_use['rent_coordinates']
        block_str = ''
        stand_str_global = ''
        for rent_block in rent_forest_use['rent_block']:
            stand_str_block = ''
            block_num = rent_block['block']['value']
            block_id = get_block_id(forestry, block_num)
            block_str = block_str + ',' + str(block_id)
            for rent_stand in rent_block['rent_stand']:
                stand_num = rent_stand['stand']['value']
                stand_str_block = stand_str_block + ',' + str(stand_num)
            stand_str_block = stand_str_block[1:]
            stand_str_global = stand_str_global + ';' + stand_str_block
        block_str = block_str[1:]
        stand_str_global = stand_str_global[1:]
        make_polygon(coordinates, plot_name, forest_use_type, block_str, stand_str_global, rent_id, leshoz)