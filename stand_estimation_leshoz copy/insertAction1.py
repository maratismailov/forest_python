import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def insert_action1(newDict, newId, modified):
    """ delete values from the stand_action table"""
    delete_action_query = """DELETE FROM forest.action WHERE standestimation_id = {}""".format(newId)
    """ insert a values into the stand_action table """
    action_query = """INSERT INTO forest.action (
        actiontype_id,
        standestimation_id,
        priority,
        modified,
        plan_fact,
        actionurgency_id,
        unit_id,
        quantity
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    action_data= (
        newDict['stand_estimation']['action_priority_1']['action_type']['code'],
        newId,
        1,
        modified,
        0,
        newDict['stand_estimation']['action_priority_1']['action_urgency']['code'],
        1,
        newDict['stand_estimation']['action_priority_1']['action_area']['value'],        
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(delete_action_query)
        cur.execute(action_query, (action_data))
        print('action')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
