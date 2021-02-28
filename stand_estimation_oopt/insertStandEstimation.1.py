import psycopg2
from insertForestComposition import insert_forest_composition
from insertPlannedForestComposition import insert_planned_forest_composition
from insertForestUseType import insert_forest_use_type
from insertPlannedForestUseType import insert_planned_forest_use_type
from insertAction1 import insert_action1
from insertAction2 import insert_action2
from insertAction1_tillage import insert_action1_tillage
from insertAction2_tillage import insert_action2_tillage
from insertAction1_creation import insert_action1_creation
from insertAction2_creation import insert_action2_creation
from insertGeometry import insert_polygon
from credentials import cr_dbname, cr_host, cr_password, cr_user
from updateForestryNum import update_forestry_num


def insert_stand_estimation(newDict):
    """get forestry_num"""
    forestry_num_query = """SELECT forestry_num from forest.forestry_full WHERE forestry_id = {} """.format(
        newDict['stand_estimation']['forestry']['code'])
    conn = psycopg2.connect(dbname=cr_dbname, user=cr_user,
                            password=cr_password, host=cr_host)
    cur = conn.cursor()
    cur.execute(forestry_num_query)
    forestry_num = cur.fetchone()[0]
    conn.commit()
    cur.close()

    leshoz = newDict['stand_estimation']['leshoz']['code']
    block = newDict['stand_estimation']['block']['value']
    stand = newDict['stand_estimation']['stand_code']['value']
    # forestry = forestry_num
    if int(leshoz) < 10:
        leshoz_str = '0' + str(leshoz)
    else:
        leshoz_str = str(leshoz)
    if int(block) < 10:
        block_str = '00' + str(block)
    elif int(block) < 100:
        block_str = '0' + str(block)
    else:
        block_str = str(block)
    if int(stand) < 10:
        stand_str = '00' + str(stand)
    elif int(stand) < 100:
        stand_str = '0' + str(stand)
    else:
        stand_str = str(stand)
    stand_code_str = str(forestry_num)+leshoz_str+block_str+stand_str
    print(stand_code_str)

    """ insert a values into the stand_test table """
    def get_stand_estimation(arg1, arg2, arg3=None):
            if arg1 not in newDict['stand_estimation'].keys():
                newDict['stand_estimation'][arg1] = None
            if arg1 == 'action_priority_1' or arg1 == 'forest_composition':
                if arg2 not in newDict['stand_estimation'][arg1].keys():
                    newDict['stand_estimation'][arg1][arg2] = None
                if newDict['stand_estimation'][arg1][arg2] is None:
                    newDict['stand_estimation'][arg1][arg2] = {arg3: None}
            elif newDict['stand_estimation'][arg1] is None:
                newDict['stand_estimation'][arg1] = {arg2: None}

    # get_stand_estimation('forest_origin', 'code')
    # get_stand_estimation('layerage', 'code')
    # get_stand_estimation('evolution_stage', 'code')
    # get_stand_estimation('exposition', 'code')
    # get_stand_estimation('age_class', 'code')
    # get_stand_estimation('crown_density', 'code')
    # get_stand_estimation('marketability_class', 'code')
    # get_stand_estimation('sanitary_class', 'code')
    # get_stand_estimation('stability', 'code')
    # get_stand_estimation('renewal_state', 'code')
    # get_stand_estimation('underbrush', 'code')
    # get_stand_estimation('cattle_pasture', 'code')
    # get_stand_estimation('forest_use_org_form', 'code')
    # get_stand_estimation('forest_use_type', 'code')
    # get_stand_estimation('burl', 'code')
    # get_stand_estimation('purpose', 'code')
    # get_stand_estimation('clutter', 'value')
    # get_stand_estimation('action_priority_1', 'action_type', 'code')
    # get_stand_estimation('action_priority_1', 'action_urgency', 'code')
    # get_stand_estimation('action_priority_1', 'action_area', 'value')
    # get_stand_estimation('action_priority_1', 'action_intensity', 'code')
    # get_stand_estimation('action_priority_1', 'planned_forest_use_org_form', 'code')
    # get_stand_estimation('action_priority_1', 'planned_forest_use_type', 'code')
    # get_stand_estimation('action_priority_1', 'tillage', 'code')
    # get_stand_estimation('action_priority_1', 'creation_type', 'code')
    # get_stand_estimation('action_priority_1', 'additionact', 'value')
    # get_stand_estimation('forest_composition', 'wood_species', 'code')
    # get_stand_estimation('forest_composition', 'species_percent', 'value')
    # get_stand_estimation('planned_forest_composition', 'wood_species', 'code')
    # get_stand_estimation('planned_forest_composition', 'species_percent', 'value')

    stand_data = (
        # newDict['stand_estimation']['stand_code']['code'],
        newDict['stand_estimation']['old_stands']['value'],
        newDict['stand_estimation']['estimation_year']['value'],
        newDict['stand_estimation']['protect_category']['code'],
        newDict['stand_estimation']['land_category']['code'],
        newDict['stand_estimation']['exploitation_category']['code'],
        newDict['stand_estimation']['exposition']['code'],
        newDict['stand_estimation']['forest_origin']['code'],
        newDict['stand_estimation']['layerage']['code'],
        newDict['stand_estimation']['evolution_stage']['code'],
        newDict['stand_estimation']['age_class']['code'],
        newDict['stand_estimation']['crown_density']['code'],
        newDict['stand_estimation']['stability']['code'],
        newDict['stand_estimation']['marketability_class']['code'],
        newDict['stand_estimation']['sanitary_class']['code'],
        newDict['stand_estimation']['renewal_state']['code'],
        newDict['stand_estimation']['underbrush']['code'],
        newDict['stand_estimation']['cattle_pasture']['code'],
        newDict['stand_estimation']['forest_use_org_form']['code'],
        newDict['stand_estimation']['burl']['code'],
        newDict['stand_estimation']['additional_info']['value'],
        newDict['stand_estimation']['purpose']['code'],
        newDict['stand_estimation']['clutter']['value'],
        newDict['stand_estimation']['forest_type']['code'],
        newDict['stand_estimation']['@modified'],
        newDict['stand_estimation']['@created'],
        stand_code_str,
        newDict['stand_estimation']['action_priority_1']['additionact']['value'],
        newDict['stand_estimation']['economic_state']['code'],
        newDict['stand_estimation']['leshoz']['code'],
        newDict['stand_estimation']['block']['value'],
        newDict['stand_estimation']['stand_code']['value'],
        1,
        newDict['stand_estimation']['cycle']['value'],
        newDict['stand_estimation']['action_priority_1']['planned_forest_use_org_form']['code'],
        25
    )

    sql = """INSERT INTO forest.standestimation (
        oldstandnums,
        estimation_year,
        protectcategory_id,
        landcategory_id, 
        exploitationcat_id, 
        exposition_id, 
        forestorigin_id, 
        layerage_id,
        evolutionstage_id, 
        ageclass_id,
        crowndensity_id, 
        stability_id, 
        marketability_id,
        sanitarystate_id, 
        renewalstate_id, 
        underbrush_id, 
        cattlepasture_id, 
        forestuseorgform_id, 
        burl_id, 
        addinfo, 
        purpose_id,
        clutter,
        foresttype_id,
        modified,
        completion_date, 
        stand_code,
        additionact1,
        economy_id,
        leshoz_id,
        block_num,
        stand_num,
        unprocessed_flag,
        cycle,
        planuseorgform1_id,
        forestry_num
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (stand_code, cycle)
        DO UPDATE SET
        ( oldstandnums,
        estimation_year,
        protectcategory_id,
        landcategory_id, 
        exploitationcat_id, 
        exposition_id, 
        forestorigin_id, 
        layerage_id,
        evolutionstage_id, 
        ageclass_id,
        crowndensity_id, 
        stability_id, 
        marketability_id,
        sanitarystate_id, 
        renewalstate_id, 
        underbrush_id, 
        cattlepasture_id, 
        forestuseorgform_id, 
        burl_id, 
        addinfo, 
        purpose_id,
        clutter,
        foresttype_id,
        modified,
        completion_date, 
        stand_code,
        additionact1,
        economy_id,
        leshoz_id,
        block_num,
        stand_num,
        unprocessed_flag,
        cycle,
        planuseorgform1_id,
        forestry_num) = {}
        RETURNING standestimation_id""".format(stand_data)
    

    conn = None
    try:
        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(forestry_num_query)
        forestry_num = cur.fetchone()[0]
        print('some')
        print(stand_data)
        print(len(stand_data))
        cur.executemany(sql, stand_data)
        print('insert success')
        newId = cur.fetchone()[0]
        print('newId is ', newId)
        modified = newDict['stand_estimation']['@modified']

        forest_compose_counter = 0
        forest_use_type_counter = 0
        # forest_geometry_counter =0

        for forest_compose in newDict['stand_estimation']['forest_composition']:
            # print(forest_compose['species_percent']['value'], 'compose')
            insert_forest_composition(
                forest_compose, newId, modified, forest_compose_counter)
            forest_compose_counter = forest_compose_counter + 1

        for forest_compose in newDict['stand_estimation']['planned_forest_composition']:
            insert_planned_forest_composition(forest_compose, newId, modified)

        for forest_use_type in newDict['stand_estimation']['forest_use_type']:
            insert_forest_use_type(
                forest_use_type, newId, modified, forest_use_type_counter)
            forest_use_type_counter = forest_use_type_counter + 1

        for forest_use_type in newDict['stand_estimation']['action_priority_1']['planned_forest_use_type']:
            priority = 0
            insert_planned_forest_use_type(
                forest_use_type, newId, modified, priority)

        # for forest_use_type in newDict['stand_estimation']['action_priority_2']['planned_forest_use_type']:
        #     priority = 1
        #     insert_planned_forest_use_type(
        #         forest_use_type, newId, modified, priority)

        insert_action1(newDict, newId, modified)
        # insert_action2(newDict, newId, modified)
        insert_action1_tillage(newDict, newId, modified)
        # insert_action2_tillage(newDict, newId, modified)
        insert_action1_creation(newDict, newId, modified)
        # insert_action2_creation(newDict, newId, modified)
        insert_polygon(newDict, stand_code_str)

        conn.commit()
        cur.close()

        update_forestry_num(newDict, newId)

        # print(newId)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
