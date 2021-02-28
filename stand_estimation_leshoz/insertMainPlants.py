import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_main_plants(plant, newId, modified, main_plants_counter):
    """ delete values from the standplant table"""
    delete_main_plants_query = """DELETE FROM forest.standplant WHERE standestimation_id = {}""".format(
        newId)
    """ insert a values into the standplant table """
    main_plants_query = """INSERT INTO forest.standplant (
        plantspecies_id,
        standestimation_id,
        modified
        )
        VALUES(%s, %s, %s)"""
    main_plants_data = (
        plant['code'],
        newId,
        modified
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if main_plants_counter == 0:
            cur.execute(delete_main_plants_query)
        cur.execute(main_plants_query, (main_plants_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
