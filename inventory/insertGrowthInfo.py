import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_growth_info(growth_info, newId, modified, growth_info_counter):
    """ delete values from the polyline table"""

    delete_growth_info_query = """DELETE FROM inv.growthinfo WHERE inventor_id = {}""".format(
        newId)
    """ insert a values into the growthinfo table """
    growth_info_query = """INSERT INTO inv.growthinfo (
        tree_num,
        woodspecies_id,
        diameter,
        ringnumber,
        length,
        age,
        modified,
        inventor_id
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    growth_info_data = (
        growth_info['tree_num']['value'],
        growth_info['wood_species']['code'],
        growth_info['diameter']['value'],
        growth_info['ring_num']['value'],
        growth_info['length']['value'],
        growth_info['age']['value'],
        modified,
        newId
    )
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if growth_info_counter == 0:
            cur.execute(delete_growth_info_query)
        cur.execute(growth_info_query, (growth_info_data))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
