import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user

def update_plants(plant, newId, modified):
    """ delete values from the standplant table"""
    select_plants_query = """SELECT standplant_id FROM forest.standplant WHERE standestimation_id = {} AND plantspecies_id = {}""".format(
        newId, plant['plant_species']['code'])
    """ insert a values into the standplant table """
    standplant_id = 0
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(select_plants_query)
        if cur.fetchone() is not None:
            cur.execute(select_plants_query)
            standplant_id = cur.fetchone()[0]
        else:
            print('is none')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    update_plants_query = """UPDATE forest.standplant SET 
                        plantspecies_id = %s,
                        plantfrequency_id = %s,
                        standestimation_id = %s,
                        modified =%s
                        WHERE standplant_id = {}""".format(standplant_id)
    insert_plants_query = """INSERT INTO forest.standplant (
        plantspecies_id,
        plantfrequency_id,
        standestimation_id,
        modified
        )
        VALUES(%s, %s, %s, %s)
        RETURNING standplant_id"""
    plants_data = (
        plant['plant_species']['code'],
        plant['plant_occurence']['code'],
        newId,
        modified
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(select_plants_query)
        if cur.fetchone() is not None:
            # standplant_id = cur.fetchone()
            cur.execute(update_plants_query, plants_data)
        else:
            cur.execute(insert_plants_query, plants_data)
            standplant_id = cur.fetchone()[0]
        # print('plantsq is', plantsq)
        # cur.execute(insert_plants_query, (plants_redflag_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return standplant_id
        
def delete_plants(plants_combined, newId, plants_delete):
    """ delete values from the standplant table"""
    delete_plants_query = """DELETE FROM forest.standplant WHERE standestimation_id = {} AND standplant_id NOT IN ({})""".format(
        newId, plants_delete)
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(delete_plants_query)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



# def delete_plants(plant, newId, modified):
#     print('plant_red_flag')
#     """ delete values from the standplant table"""
#     delete_plants_redflag_query = """DELETE FROM forest.standplant WHERE standestimation_id = {}""".format(
#         newId)
#     """ insert a values into the standplant table """
#     plants_redflag_query = """INSERT INTO forest.standplant (
#         plantspecies_id,
#         plantfrequency_id,
#         standestimation_id,
#         modified
#         )
#         VALUES(%s, %s, %s, %s)"""
#     plants_redflag_data = (
#         plant['plant_species_redflag']['code'],
#         plant['plant_occurence']['code'],
#         newId,
#         modified
#     )
#     conn = None
#     try:
#         conn = psycopg2.connect(
#             dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
#         cur = conn.cursor()
#         # if plant_redflag_counter == 0:
#         #     cur.execute(delete_plants_redflag_query)
#         cur.execute(plants_redflag_query, (plants_redflag_data))
#         conn.commit()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
