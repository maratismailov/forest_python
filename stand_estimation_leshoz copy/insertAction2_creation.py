import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_action2_creation(newDict, newId, modified):
    """ insert a values into the stand_action table """
    action_query = """INSERT INTO forest.action (
        actiontype_id,
        standestimation_id,
        priority,
        modified,
        plan_fact
        )
        VALUES(%s, %s, %s, %s, %s)"""
    action_data= (
        newDict['stand_estimation']['action_priority_2']['creation_type']['code'],
        newId,
        1,
        modified,
        0,
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
