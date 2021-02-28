import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_plants_redflag(plant, newId, modified, plant_redflag_counter):
    """ delete values from the standplant table"""
    delete_plants_redflag_query = """DELETE FROM forest.standplant WHERE standestimation_id = {}""".format(
        newId)
    """ insert a values into the standplant table """
    plants_redflag_query = """INSERT INTO forest.standplant (
        plantspecies_id,
        plantfrequency_id,
        standestimation_id,
        modified
        )
        VALUES(%s, %s, %s, %s)"""
    plants_redflag_data = (
        plant['plant_species_redflag']['code'],
        plant['plant_occurence']['code'],
        newId,
        modified
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if plant_redflag_counter == 0:
            cur.execute(delete_plants_redflag_query)
        cur.execute(plants_redflag_query, (plants_redflag_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
