import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def insert_action1(action, newId, modified, action_counter):
    """ delete values from the stand_action table"""
    delete_action_query = """DELETE FROM forest.action WHERE standestimation_id = {}""".format(newId)
    """ insert a values into the stand_action table """
    action_query = """INSERT INTO forest.action (
        actiontype_id,
        intensity,
        standestimation_id,
        priority,
        modified,
        plan_fact,
        actionurgency_id,
        unit_id,
        quantity,
        f_type
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    action_data= (
        action['action_type']['code'],
        action['action_intensity']['code'],
        newId,
        1,
        modified,
        0,
        action['action_urgency']['code'],
        1,
        action['action_area']['value'],        
        'f25'
    )
    print(action_data)
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if action_counter == 0:
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
