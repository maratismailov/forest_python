import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_ecoproblem(ecoproblem, newId, modified, ecoproblems_counter):
    """ delete values from the ecoproblem table"""

    delete_ecoproblem_query = """DELETE FROM forest.ecoproblem WHERE standestimation_id = {}""".format(
        newId)
    """ insert a values into the ecoproblem table """
    ecoproblemquery = """INSERT INTO forest.ecoproblem (
        ecoproblemtype_id,
        ecoproblemseverity_id,
        standestimation_id,
        modified
        )
        VALUES(%s, %s, %s, %s)"""
    ecoproblem_data = (
        ecoproblem['ecoproblem_type']['code'],
        ecoproblem['ecoproblemseverity']['code'],
        newId,
        modified
    )
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if ecoproblems_counter == 0:
            cur.execute(delete_ecoproblem_query)
        cur.execute(ecoproblemquery, (ecoproblem_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
