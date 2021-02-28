import psycopg2
from stand_estimation_oopt.insertForestComposition import insert_forest_composition
from stand_estimation_oopt.insertEcoproblems import insert_ecoproblem
from stand_estimation_oopt.insertPlants import update_plants, delete_plants
from stand_estimation_oopt.insertAnimalsRedflag import insert_animals_redflag
from stand_estimation_oopt.insertPlannedForestComposition import insert_planned_forest_composition
from stand_estimation_oopt.insertForestUseType import insert_forest_use_type
from stand_estimation_oopt.insertPlannedForestUseType import insert_planned_forest_use_type
from stand_estimation_oopt.insertAction1 import insert_action1
from stand_estimation_oopt.insertAction2 import insert_action2
from stand_estimation_oopt.insertAction1_tillage import insert_action1_tillage
from stand_estimation_oopt.insertAction2_tillage import insert_action2_tillage
from stand_estimation_oopt.insertAction1_creation import insert_action1_creation
from stand_estimation_oopt.insertAction2_creation import insert_action2_creation
from stand_estimation_oopt.insertGeometry import insert_polygon
from credentials import cr_dbname, cr_host, cr_password, cr_user
import sys
# from updateForestryNum import update_forestry_num


def insert_stand_estimation_oopt(newDict):
    def get_stand_estimation(arg1, arg2):
        if arg1 not in newDict['stand_estimation'].keys():
            newDict['stand_estimation'][arg1] = {arg2: None}
            # print('not arg1', arg1)
        elif newDict['stand_estimation'][arg1] is None:
            newDict['stand_estimation'][arg1] = {arg2: None}
            # print('arg1 none', arg1)

    # def get_long_stand_estimation(arg1, arg2, arg3=None):
    #     print(arg2)
    #     if arg1 not in newDict['stand_estimation'].keys():
    #         newDict['stand_estimation'][arg1] = {arg2: {arg3: None}}
        # elif arg2 not in newDict['stand_estimation'][arg1].keys():
        #     newDict['stand_estimation'][arg1][arg2] = {arg3: None}
        # elif newDict['stand_estimation'][arg1][arg2] is None:
        #     newDict['stand_estimation'][arg1][arg2] = {arg3: None}

    get_stand_estimation('old_block', 'value')
    get_stand_estimation('old_stands', 'value')
    get_stand_estimation('additional_info', 'value')

    """get forestry_num"""
    forestry_num_query = """SELECT forestry_num from forest.forestry WHERE gid = {} """.format(
        newDict['stand_estimation']['zone']['code'])
    conn = psycopg2.connect(dbname=cr_dbname, user=cr_user,
                            password=cr_password, host=cr_host)
    cur = conn.cursor()
    cur.execute(forestry_num_query)
    forestry_num = cur.fetchone()[0]
    conn.commit()
    cur.close()

    leshoz = newDict['stand_estimation']['oopt']['code']
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

    """insert and select block_id"""
    block_data = (
        newDict['stand_estimation']['zone']['code'],
        newDict['stand_estimation']['block']['value']
    )
    # check_for_block_query = """SELECT gid from forest.block WHERE forestry_id = {} AND block_num = {}""".format(
    #     forestry_num,
    #     newDict['stand_estimation']['block']['value'])
    check_for_block_query = """SELECT gid from forest.block WHERE forestry_id = {} AND block_num = {}""".format(
        newDict['stand_estimation']['zone']['code'],
        newDict['stand_estimation']['block']['value'])
    insert_block_query = """INSERT INTO forest.block (
        forestry_id,
        block_num
        )
        VALUES(%s, %s)
        RETURNING gid"""
    conn = psycopg2.connect(dbname=cr_dbname, user=cr_user,
                            password=cr_password, host=cr_host)
    cur = conn.cursor()
    cur.execute(check_for_block_query)
    isBlock = cur.rowcount
    if isBlock == 0:
        cur.execute(insert_block_query, block_data)
        block_id = cur.fetchone()[0]
        # print('block_id is ', block_id)
    else:
        cur.execute(check_for_block_query)
        block_id = cur.fetchone()[0]
        # print('block_id is ', block_id)
    # print('isBlock is ', isBlock)

    conn.commit()
    cur.close()

    """ insert a values into the stand_test table """
    # def get_stand_estimation(arg1, arg2):
    #     if arg1 not in newDict['stand_estimation'].keys():
    #         newDict['stand_estimation'][arg1] = {arg2: None}
    #         # print('not arg1', arg1)
    #     elif newDict['stand_estimation'][arg1] is None:
    #         newDict['stand_estimation'][arg1] = {arg2: None}
    #         # print('arg1 none', arg1)

    # def get_long_stand_estimation(arg1, arg2, arg3=None):
    #     if arg1 not in newDict['stand_estimation'].keys():
    #         newDict['stand_estimation'][arg1] = {arg2: {arg3: None}}
    #     elif arg2 not in newDict['stand_estimation'][arg1].keys():
    #         newDict['stand_estimation'][arg1][arg2] = {arg3: None}
    #     elif newDict['stand_estimation'][arg1][arg2] is None:
    #         newDict['stand_estimation'][arg1][arg2] = {arg3: None}

    # def get_forest_composition(arg1, arg2, arg3=None):
    #     if arg1 not in newDict['stand_estimation'].keys():
    #         newDict['stand_estimation'][arg1] = {arg2: {arg3: None}}
    # else:
    #     for compose in newDict['stand_estimation'][arg1]:
    #         print('compose is ', compose)
    # elif arg2 not in newDict['stand_estimation'][arg1]:
    #     newDict['stand_estimation'][arg1][arg2] = {arg3: None}
    # elif newDict['stand_estimation'][arg1][arg2] is None:
    #     newDict['stand_estimation'][arg1][arg2] = {arg3: None}

    # def get_forest_use_type(arg1, arg2):
    #     print(len(newDict['stand_estimation'][arg1]))
    #     if len(newDict['stand_estimation'][arg1]) > 0:
    #         print('big')
    #     else:
    #         print('small')

    get_stand_estimation('old_stands', 'value')
    get_stand_estimation('protect_category', 'code')
    get_stand_estimation('land_category', 'code')
    get_stand_estimation('exploitation_category', 'code')
    get_stand_estimation('exposition', 'code')
    get_stand_estimation('forest_origin', 'code')
    get_stand_estimation('layerage', 'code')
    get_stand_estimation('evolution_stage', 'code')
    get_stand_estimation('age_class', 'code')
    get_stand_estimation('crown_density', 'code')
    get_stand_estimation('stability', 'code')
    get_stand_estimation('marketability_class', 'code')
    get_stand_estimation('sanitary_class', 'code')
    get_stand_estimation('renewal_state', 'code')
    get_stand_estimation('underbrush', 'code')
    get_stand_estimation('cattle_pasture', 'code')
    get_stand_estimation('forest_use_org_form', 'code')
    get_stand_estimation('burl', 'code')
    get_stand_estimation('additional_info', 'value')
    get_stand_estimation('firehazardclass', 'code')
    get_stand_estimation('planned_roads', 'value')
    get_stand_estimation('steepness', 'value')
    get_stand_estimation('land_category_f46_1', 'code')
    get_stand_estimation('peoplevisit', 'code')
    get_stand_estimation('potentialtour', 'code')
    get_stand_estimation('purpose', 'code')
    get_stand_estimation('clutter', 'value')
    get_stand_estimation('forest_type', 'code')
    get_stand_estimation('economic_state', 'code')
    get_stand_estimation('oopt', 'code')
    get_stand_estimation('block', 'value')
    get_stand_estimation('stand_code', 'value')
    get_stand_estimation('cycle', 'value')
    get_stand_estimation('planned_forest_use_org_form', 'code')

    # get_long_stand_estimation('action_priority_1', 'action_type', 'code')
    # get_long_stand_estimation('action_priority_1', 'action_urgency', 'code')
    # get_long_stand_estimation('action_priority_1', 'action_area', 'value')
    # get_long_stand_estimation('action_priority_1', 'action_intensity', 'code')
    # get_long_stand_estimation('action_priority_1',
    #                           'planned_forest_use_org_form', 'code')
    # get_long_stand_estimation('action_priority_1',
    #                           'planned_forest_use_type', 'code')
    # get_long_stand_estimation('action_priority_1', 'tillage', 'code')
    # get_long_stand_estimation('action_priority_1', 'creation_type', 'code')
    # get_long_stand_estimation('action_priority_1', 'additionact', 'value')
    # get_long_stand_estimation('ecoproblems', 'ecoproblem_type', 'code')
    # get_long_stand_estimation('ecoproblems', 'ecoproblemseverity', 'code')
    # get_long_stand_estimation('plant_redflag', 'plant_species_redflag', 'code')
    # get_long_stand_estimation('plant_redflag', 'plant_occurence', 'code')
    # get_long_stand_estimation(
    #     'animal_redflag', 'animal_species_redflag', 'code')
    # get_long_stand_estimation('animal_redflag', 'animal_occurence', 'code')
    # # get_long_stand_estimation('main', 'ecoproblemseverity', 'code')

    # get_forest_composition('forest_composition', 'wood_species', 'code')
    # get_forest_composition('forest_composition', 'species_percent', 'value')
    # get_forest_composition(
    #     'planned_forest_composition', 'wood_species', 'code')
    # get_forest_composition('planned_forest_composition',
    #                        'species_percent', 'value')
    # print(newDict)

    stand_data = (
        # newDict['stand_estimation']['stand_code']['code'],
        newDict['stand_estimation']['old_stands']['value'],
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
        newDict['stand_estimation']['firehazardclass']['code'],
        newDict['stand_estimation']['planned_roads']['value'],
        newDict['stand_estimation']['steepness']['value'],
        newDict['stand_estimation']['land_category_f46_1']['code'],
        newDict['stand_estimation']['peoplevisit']['code'],
        newDict['stand_estimation']['potentialtour']['code'],
        newDict['stand_estimation']['purpose']['code'],
        newDict['stand_estimation']['clutter']['value'],
        newDict['stand_estimation']['forest_type']['code'],
        newDict['stand_estimation']['@modified'],
        newDict['stand_estimation']['@created'],
        stand_code_str,
        newDict['stand_estimation']['economic_state']['code'],
        newDict['stand_estimation']['oopt']['code'],
        newDict['stand_estimation']['block']['value'],
        newDict['stand_estimation']['stand_code']['value'],
        1,
        newDict['stand_estimation']['cycle']['value'],
        newDict['stand_estimation']['planned_forest_use_org_form']['code'],
        forestry_num,
        newDict['stand_estimation']['old_stands']['value'],
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
        newDict['stand_estimation']['firehazardclass']['code'],
        newDict['stand_estimation']['planned_roads']['value'],
        newDict['stand_estimation']['steepness']['value'],
        newDict['stand_estimation']['land_category_f46_1']['code'],
        newDict['stand_estimation']['peoplevisit']['code'],
        newDict['stand_estimation']['potentialtour']['code'],
        newDict['stand_estimation']['purpose']['code'],
        newDict['stand_estimation']['clutter']['value'],
        newDict['stand_estimation']['forest_type']['code'],
        newDict['stand_estimation']['@modified'],
        newDict['stand_estimation']['@created'],
        stand_code_str,
        newDict['stand_estimation']['economic_state']['code'],
        newDict['stand_estimation']['oopt']['code'],
        newDict['stand_estimation']['block']['value'],
        newDict['stand_estimation']['stand_code']['value'],
        1,
        newDict['stand_estimation']['cycle']['value'],
        newDict['stand_estimation']['planned_forest_use_org_form']['code'],
        forestry_num
    )
    sql = """INSERT INTO forest.standestimation (
        oldstandnums,
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
        firehazardclass_id,
        projectroad,
        steepness,
        landtype_id,
        peoplevisit_id,
        potentialtour_id,
        purpose_id,
        clutter,
        foresttype_id,
        modified,
        completion_date,
        stand_code,
        economy_id,
        leshoz_id,
        block_num,
        stand_num,
        unprocessed_flag,
        cycle,
        planuseorgform1_id,
        forestry_num
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (stand_code, cycle)
        DO UPDATE SET
        oldstandnums = %s,
        protectcategory_id = %s,
        landcategory_id = %s,
        exploitationcat_id = %s,
        exposition_id = %s,
        forestorigin_id = %s,
        layerage_id = %s,
        evolutionstage_id = %s,
        ageclass_id = %s,
        crowndensity_id = %s,
        stability_id = %s,
        marketability_id = %s,
        sanitarystate_id = %s,
        renewalstate_id = %s,
        underbrush_id = %s,
        cattlepasture_id = %s,
        forestuseorgform_id = %s,
        burl_id = %s,
        addinfo = %s,
        firehazardclass_id = %s,
        projectroad = %s,
        steepness = %s,
        landtype_id = %s,
        peoplevisit_id = %s,
        potentialtour_id = %s,
        purpose_id = %s,
        clutter = %s,
        foresttype_id = %s,
        modified = %s,
        completion_date = %s,
        stand_code = %s,
        economy_id = %s,
        leshoz_id = %s,
        block_num = %s,
        stand_num = %s,
        unprocessed_flag = %s,
        cycle = %s,
        planuseorgform1_id = %s,
        forestry_num = %s
        RETURNING standestimation_id"""
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(forestry_num_query)
        forestry_num = cur.fetchone()[0]
        cur.execute(sql, stand_data)
        print('insert successsssss')
        newId = cur.fetchone()[0]
        print('newId is ', newId)
        modified = newDict['stand_estimation']['@modified']
        forest_compose_counter = 0
        forest_use_type_counter = 0
        planned_forest_use_type_counter = 0
        ecoproblems_counter = 0
        animal_redflag_counter = 0
        action_counter = 0
        tillage_1_counter = 0
        creation_1_counter = 0

        if 'forest_composition' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for forest_compose in newDict['stand_estimation']['forest_composition']:
                    insert_forest_composition(
                        forest_compose, newId, modified, forest_compose_counter)
                    forest_compose_counter = forest_compose_counter + 1
            except:
                print('empty')

        if 'ecoproblems' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for ecoproblem in newDict['stand_estimation']['ecoproblems']:
                    insert_ecoproblem(
                        ecoproblem, newId, modified, ecoproblems_counter)
                    ecoproblems_counter = ecoproblems_counter + 1
            except:
                print('empty')

        plants_combined = []
        main_plants_extended = []
        red_plants_extended = []

        if 'main_plants' in newDict['stand_estimation'].keys():
            for plant in newDict['stand_estimation']['main_plants']:
                specie_code = dict(plant)['code']
                main_plants_extended.append(
                    {'plant_species': {'code': specie_code}, 'plant_occurence': {'code': None}})
        if 'plant_redflag' in newDict['stand_estimation'].keys():
            for plant in newDict['stand_estimation']['plant_redflag']:
                specie_code = dict(plant)['plant_species_redflag']['code']
                specie_occurence = dict(plant)['plant_occurence']['code']
                red_plants_extended.append({'plant_species': {
                                           'code': specie_code}, 'plant_occurence': {'code': specie_occurence}})
        plants_combined = main_plants_extended + red_plants_extended

        try:
            pre_plants_delete = ''
            for plant in plants_combined:
                # plants_delete = update_plants(plant, newId, modified)
                pre_plants_delete += str(update_plants(plant,
                                                       newId, modified)) + ','
                # update_plants(plant, newId, modified)
            if len(pre_plants_delete) > 1:
                plants_delete = pre_plants_delete[:-1]
            delete_plants(plants_combined, newId, plants_delete)
        except:
            print('empty***')

        #     plants_combined = plants_combined + newDict['stand_estimation']['plant_redflag']
        # if 'main_plants' in newDict['stand_estimation'].keys():
        #     plants_combined = plants_combined + newDict['stand_estimation']['main_plants']

        # if len(plants_combined) > 0:
        #     print(plants_combined)
        #     try:
        #         for plant in plants_combined:
        #             print(plant)
        #             insert_main_plants(
        #                 plant, newId, modified, main_plants_counter)
        #             main_plants_counter = main_plants_counter + 1
        #     except:
        #         print('empty')
        # else:
        #     print('empty')

        # if 'plant_redflag' not in newDict['stand_estimation'].keys():
        #         print('empty')
        # else:
        #     try:
        #         for plant in newDict['stand_estimation']['plant_redflag']:
        #             insert_plants_redflag(
        #                 plant, newId, modified)
        #     except:
        #         print('empty')

        # if 'main_plants' not in newDict['stand_estimation'].keys():
        #     print('empty')
        # else:
        #     try:
        #         for plant in newDict['stand_estimation']['main_plants']:
        #             insert_main_plants(
        #                 plant, newId, modified)
        #     except:
        #         print('empty')

        if 'animal_redflag' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for animal in newDict['stand_estimation']['animal_redflag']:
                    insert_animals_redflag(
                        animal, newId, modified, animal_redflag_counter)
                    animal_redflag_counter = animal_redflag_counter + 1
            except:
                print('empty')

        if 'planned_forest_use_type' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for forest_use_type in newDict['stand_estimation']['planned_forest_use_type']:
                    priority = 0
                    insert_planned_forest_use_type(
                        forest_use_type, newId, modified, priority, planned_forest_use_type_counter)
                    planned_forest_use_type_counter = planned_forest_use_type_counter + 1
            except:
                print('empty')

        if 'forest_use_type' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for forest_use_type in newDict['stand_estimation']['forest_use_type']:
                    insert_forest_use_type(
                        forest_use_type, newId, modified, forest_use_type_counter)
                    forest_use_type_counter = forest_use_type_counter + 1
            except:
                print('empty')

        if 'action_priority_1' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for actions in newDict['stand_estimation']['action_priority_1']:
                    print(actions)
                    priority = 0
                    insert_action1(
                        actions, newId, modified, action_counter)
                    action_counter = action_counter + 1
            except:
                print('empty')

        if 'tillage_1' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for tillage in newDict['stand_estimation']['tillage_1']:
                    priority = 1
                    insert_action1_tillage(
                        tillage, newId, modified, tillage_1_counter)
                    tillage_1_counter = tillage_1_counter + 1
            except:
                print('empty')

        if 'creation_type_1' not in newDict['stand_estimation'].keys():
            print('empty')
        else:
            try:
                for creation in newDict['stand_estimation']['creation_type_1']:
                    priority = 1
                    insert_action1_creation(
                        creation, newId, modified, creation_1_counter)
                    creation_1_counter = creation_1_counter + 1
            except:
                print('empty')

        insert_polygon(newDict, stand_code_str, forestry_num, block_id)
        conn.commit()
        cur.close()
        print('sss')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
