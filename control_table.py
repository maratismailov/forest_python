import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

""" get data from surveytype """
is_develop = 1

get_path_query = """SELECT path FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_leshoz_path_query = """SELECT stand_est_leshoz_path FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_oopt_path_query = """SELECT stand_est_oopt_path FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_inv_path_query = """SELECT inventory_path FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_geodata_rent_path_query = """SELECT geodata_rent_path FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_path_to_remove_query = """SELECT path_to_remove FROM control.paths WHERE is_develop = {}""".format(is_develop)
get_path_to_copy_query = """SELECT path_to_copy FROM control.paths WHERE is_develop = {}""".format(is_develop)


conn = None
try:
    conn = psycopg2.connect(
        dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
    cur = conn.cursor()

    cur.execute(get_path_query)
    path = cur.fetchone()[0]

    cur.execute(get_leshoz_path_query)
    lezhoz_path = cur.fetchone()[0]

    cur.execute(get_oopt_path_query)
    oopt_path = cur.fetchone()[0]

    cur.execute(get_inv_path_query)
    inv_path = cur.fetchone()[0]

    cur.execute(get_geodata_rent_path_query)
    geodata_rent_path = cur.fetchone()[0]

    cur.execute(get_path_to_remove_query)
    path_to_remove = cur.fetchone()[0]

    cur.execute(get_path_to_copy_query)
    path_to_copy = cur.fetchone()[0]

    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
