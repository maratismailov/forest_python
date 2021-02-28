import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def insert_action1_creation(creation, newId, modified, action_counter, priority):
    """ insert values into the stand_action table """
    action_query = """INSERT INTO forest.action (
        actiontype_id,
        standestimation_id,
        priority,
        modified,
        plan_fact,
        f_type
        )
        VALUES(%s, %s, %s, %s, %s, %s)"""
    action_data= (
        str(int(creation['code']) + 63),
        newId,
        priority,
        modified,
        0,
        'f32'
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(action_query, (action_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
