import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def insert_planned_forest_use_type(forest_use_type, newId, modified, priority, forest_use_type_counter):
    """ delete values from the stand_action table"""
    delete_forest_use_type_query = """DELETE FROM forest.standforestuse WHERE standestimation_id = {} AND plan_fact = 0""".format(newId)
    """ insert a values into the stand_test table """
    forest_use_type_query = """INSERT INTO forest.standforestuse (
        standestimation_id,
        forestusetype_id,
        priority,
        plan_fact,
        modified
        )
        VALUES(%s, %s, %s, %s, %s)"""
    forest_use_type_data= (
        newId,
        forest_use_type['code'],
        priority,
        0,
        modified
    )
    conn = None
    try:
        print('bam', forest_use_type_counter)
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if forest_use_type_counter == 0:
            cur.execute(delete_forest_use_type_query)
        cur.execute(forest_use_type_query, (forest_use_type_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
