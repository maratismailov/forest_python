import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_bush_species(bush_species, newId, modified, bush_species_counter):
    """ delete values from the inventbush table"""

    delete_bush_species_query = """DELETE FROM inv.inventbush WHERE inventor_id = {}""".format(
        newId)
    """ insert a values into the inventbush table """
    bush_species_query = """INSERT INTO inv.inventbush (
        bushspecies_id,
        bushheight,
        modified,
        inventor_id
        )
        VALUES(%s, %s, %s, %s)"""
    bush_species_data = (
        bush_species['bush_species']['code'],
        bush_species['bush_height']['value'],
        modified,
        newId
    )
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if bush_species_counter == 0:
            cur.execute(delete_bush_species_query)
        cur.execute(bush_species_query, (bush_species_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
