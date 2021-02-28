import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_animals_redflag(animal, newId, modified, plant_redflag_counter):
    """ delete values from the standanimal table"""
    delete_animals_redflag_query = """DELETE FROM forest.standanimal WHERE standestimation_id = {}""".format(
        newId)
    """ insert a values into the standplant table """
    animals_redflag_query = """INSERT INTO forest.standanimal (
        animalspecies_id,
        animalfrequency_id,
        standestimation_id,
        modified
        )
        VALUES(%s, %s, %s, %s)"""
    animals_redflag_data = (
        animal['animal_species_redflag']['code'],
        animal['animal_occurence']['code'],
        newId,
        modified
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if plant_redflag_counter == 0:
            cur.execute(delete_animals_redflag_query)
        cur.execute(animals_redflag_query, (animals_redflag_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
