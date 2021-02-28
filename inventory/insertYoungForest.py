import psycopg2
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_young_forest(young_forest, newId, modified, young_forest_counter):
    """ delete values from the youngforest table"""
    print('cl1')
    delete_young_forest_query = """DELETE FROM inv.youngforest WHERE inventor_id = {}""".format(
        newId)
    """ insert a values into the youngforest table """
    young_forest_query = """INSERT INTO inv.youngforest (
        woodspecies_id,
        cl1seedsur,
        cl2seedsur,
        cl3seedsur,
        cl4seedsur,
        cl5seedsur,
        cl1seedunr,
        cl2seedunr,
        cl3seedunr,
        cl4seedunr,
        cl5seedunr,
        cl1vegesur,
        cl2vegesur,
        cl3vegesur,
        cl4vegesur,
        cl5vegesur,
        cl1vegeunr,
        cl2vegeunr,
        cl3vegeunr,
        cl4vegeunr,
        cl5vegeunr,
        modified,
        inventor_id
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    young_forest_data = (
        young_forest['wood_species']['code'],
        young_forest['cl1']['cl1_seed_sur']['value'],
        young_forest['cl2']['cl2_seed_sur']['value'],
        young_forest['cl3']['cl3_seed_sur']['value'],
        young_forest['cl4']['cl4_seed_sur']['value'],
        young_forest['cl4_height']['cl4_seed_sur']['value'],
        young_forest['cl1']['cl1_seed_unr']['value'],
        young_forest['cl2']['cl2_seed_unr']['value'],
        young_forest['cl3']['cl3_seed_unr']['value'],
        young_forest['cl4']['cl4_seed_unr']['value'],
        young_forest['cl4_height']['cl4_seed_unr']['value'],
        young_forest['cl1']['cl1_vege_sur']['value'],
        young_forest['cl2']['cl2_vege_sur']['value'],
        young_forest['cl3']['cl3_vege_sur']['value'],
        young_forest['cl4']['cl4_vege_sur']['value'],
        young_forest['cl4_height']['cl4_vege_sur']['value'],
        young_forest['cl1']['cl1_vege_unr']['value'],
        young_forest['cl2']['cl2_vege_unr']['value'],
        young_forest['cl3']['cl3_vege_unr']['value'],
        young_forest['cl4']['cl4_vege_unr']['value'],
        young_forest['cl4_height']['cl4_vege_unr']['value'],
        modified,
        newId
    )
    print(young_forest_data)
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        if young_forest_counter == 0:
            cur.execute(delete_young_forest_query)
        cur.execute(young_forest_query, (young_forest_data))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
