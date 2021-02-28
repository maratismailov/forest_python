import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def insert_planned_forest_composition(forest_compose, newId, modified, forest_compose_counter):
    """ delete values from the stand_action table"""
    delete_forest_compose_query = """DELETE FROM forest.forestcomposition WHERE standestimation_id = {}""".format(newId)
    """ insert a values into the stand_action table """
    forest_composition = """INSERT INTO forest.forestcomposition (
        woodspecies_id,
        standestimation_id,
        species_percent,
        plan_fact,
        modified
        )
        VALUES(%s, %s, %s, %s, %s)"""
    composition_data = (
       forest_compose['wood_species']['code'],
       newId,
       forest_compose['species_percent']['value'],
        0,
        modified
        )
    conn = None
    try:
        conn = psycopg2.connect(dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if forest_compose_counter == 0:
            cur.execute(delete_forest_compose_query)
        cur.execute(forest_composition, (composition_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()