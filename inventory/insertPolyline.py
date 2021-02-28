import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_polyline(polyline, newId, modified, polyline_counter):
    """ delete values from the polyline table"""

    delete_polyline_query = """DELETE FROM inv.polyline WHERE inventor_id = {}""".format(
        newId)
    """ insert a values into the polyline table """
    polyline_query = """INSERT INTO inv.polyline (
        pointnum,
        height,
        asimuth,
        mapdist,
        fielddist,
        modified,
        inventor_id
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    polyline_data = (
        polyline['point_number']['value'],
        polyline['height']['value'],
        polyline['azimuth']['value'],
        polyline['distance_on_map']['value'],
        polyline['distance_on_field']['value'],
        modified,
        newId
    )
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if polyline_counter == 0:
            cur.execute(delete_polyline_query)
        cur.execute(polyline_query, (polyline_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
