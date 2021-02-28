import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def delete_stand_estimation():
    """ delete values from forest.standestimation_test """
    sql = """DELETE FROM forest.standestimation WHERE stand_code = 202027069"""
    # sql = """DELETE FROM forest.standestimation WHERE standestimation_id = 3305"""
    # sql = """DELETE FROM forest.action WHERE standestimation_id = 3306"""
    # sql = """DELETE FROM forest.standforestuse WHERE standestimation_id = 3306"""


    
    conn = None
    try:
        conn = psycopg2.connect(dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
delete_stand_estimation()