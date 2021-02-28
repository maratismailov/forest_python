import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def update_forestry_num(newDict, newId):
    """get forestry_num"""
    try:
        get_forestry_num_query = """SELECT forestry_num from forest.forestry_full WHERE forestry_id = {} """.format(
            newDict['stand_estimation']['forestry']['code'])
        conn = psycopg2.connect(dbname=cr_dbname, user=cr_user,
                                password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(get_forestry_num_query)
        forestry_num = cur.fetchone()[0]
        # conn.commit()
        # cur.close()

        """ update a forestry_num values into the standestimation"""
        update_forestry_num_query = """UPDATE forest.standestimation SET forestry_num = {} WHERE standestimation_id = {}""".format(forestry_num, newId)
    # conn = None
        # conn = psycopg2.connect(dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        # cur = conn.cursor()
        print(newId, 'newId')
        cur.execute(update_forestry_num_query)
        conn.commit()
        cur.close()
        print('forestry', forestry_num, newId)
        print('query', update_forestry_num_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
