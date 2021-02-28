import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_timber_counting(timber_counting, newId, modified, timber_counting_counter):
    """ delete values from the timber_counting table"""

    delete_timber_counting_query = """DELETE FROM inv.timbercounting WHERE inventor_id = {}""".format(
        newId)
    """ insert a values into the timbercounting table """
    timber_counting_query = """INSERT INTO inv.timbercounting (
        tree_num,
        azimuth,
        distance,
        woodspecies_id,
        diameter,
        height,
        tier,
        tree_cl,
        damageplace,
        damagereason,
        marketlength,
        rootburl,
        trunkburl,
        note,
        modified,
        inventor_id
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    timber_counting_data = (
        timber_counting['tree_num']['value'],
        timber_counting['azimuth']['value'],
        timber_counting['distance']['value'],
        timber_counting['wood_species']['code'],
        timber_counting['diameter']['value'],
        timber_counting['height']['value'],
        timber_counting['tier']['code'],
        timber_counting['tree_cl']['code'],
        timber_counting['damage_place']['code'],
        timber_counting['damage_reason']['code'],
        timber_counting['market_length']['code'],
        timber_counting['root_burl']['code'],
        timber_counting['trunk_burl']['code'],
        timber_counting['note']['value'],
        modified,
        newId
    )
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if timber_counting_counter == 0:
            cur.execute(delete_timber_counting_query)
        cur.execute(timber_counting_query, (timber_counting_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
