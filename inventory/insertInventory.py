import psycopg2
import json
from insertPolyline import insert_polyline
from insertGrowthInfo import insert_growth_info
from insertBushSpecies import insert_bush_species
from insertTimberCounting import insert_timber_counting
from insertYoungForest import insert_young_forest
from credentials import cr_dbname, cr_host, cr_password, cr_user


def insert_inventory(newDict):

    def get_inventory(arg1, arg2):
        if arg1 not in newDict['sample_plot_inventory'].keys():
            newDict['sample_plot_inventory'][arg1] = {arg2: None}
        elif newDict['sample_plot_inventory'][arg1] is None:
            newDict['sample_plot_inventory'][arg1] = {arg2: None}

        
    def get_nested_inventory(arg1, arg2, arg3):
        if arg1 not in newDict['sample_plot_inventory'].keys():
            newDict['sample_plot_inventory'][arg1] = {arg2: {arg3: None}}
        else:
            try:
                a = newDict['sample_plot_inventory'][arg1][arg2][arg3]
            except:
                newDict['sample_plot_inventory'][arg1][arg2] = {arg3: None}


    def get_deep_nested_inventory(arg1, arg2, arg3, arg4):
        if arg1 not in newDict['sample_plot_inventory'].keys():
            newDict['sample_plot_inventory'][arg1] = {arg2: {arg3: {arg4: None}}}
        else:
            try:
                a = newDict['sample_plot_inventory'][arg1][arg2][arg3][arg4]
            except:
                newDict['sample_plot_inventory'][arg1][arg2][arg3] = {arg4: None}
    
    # def get_empty(arg1, arg2, arg3):
    #     if arg1 not in newDict['sample_plot_inventory'].keys():
    #         newDict['sample_plot_inventory'][arg1] = {arg2: {arg3: None}}
    #     elif arg2

    # def get_deep_empty(arg1, arg2, arg3, arg4):
    #     if arg1 not in newDict['sample_plot_inventory'].keys():
    #         newDict['sample_plot_inventory'][arg1] = {arg2: {arg3: {arg4: None}}}


    # get_empty('polyline', 'point_number', 'value')
    # get_empty('polyline', 'height', 'value')
    # get_empty('polyline', 'azimuth', 'value')
    # get_empty('polyline', 'distance_on_map', 'value')
    # get_empty('polyline', 'distance_on_field', 'value')
    # get_empty('growth_info', 'tree_num', 'value')
    # get_empty('growth_info', 'wood_species', 'code')
    # get_empty('growth_info', 'diameter', 'value')
    # get_empty('growth_info', 'ring_num', 'value')
    # get_empty('growth_info', 'length', 'value')
    # get_empty('growth_info', 'age', 'value')
    # get_empty('bush_species', 'bush_species', 'code')
    # get_empty('bush_species', 'bush_height', 'value')
    # get_empty('timber_counting', 'tree_num', 'value')
    # get_empty('timber_counting', 'azimuth', 'value')
    # get_empty('timber_counting', 'distance', 'value')
    # get_empty('timber_counting', 'wood_species', 'code')
    # get_empty('timber_counting', 'diameter', 'value')
    # get_empty('timber_counting', 'height', 'value')
    # get_empty('timber_counting', 'tier', 'code')
    # get_empty('timber_counting', 'tree_cl', 'code')
    # get_empty('timber_counting', 'damage_place', 'code')
    # get_empty('timber_counting', 'damage_reason', 'code')
    # get_empty('timber_counting', 'market_length', 'code')
    # get_empty('timber_counting', 'root_burl', 'code')
    # get_empty('timber_counting', 'trunk_burl', 'code')
    # get_empty('timber_counting', 'note', 'value')

    # get_deep_empty('young_forest', 'cl1', 'cl1_seed_sur', 'value')
    # get_deep_empty('young_forest', 'cl1', 'cl1_seed_unr', 'value')
    # get_deep_empty('young_forest', 'cl1', 'cl1_vege_sur', 'value')
    # get_deep_empty('young_forest', 'cl1', 'cl1_vege_unr', 'value')
    # get_deep_empty('young_forest', 'cl2', 'cl2_seed_sur', 'value')
    # get_deep_empty('young_forest', 'cl2', 'cl2_seed_unr', 'value')
    # get_deep_empty('young_forest', 'cl2', 'cl2_vege_sur', 'value')
    # get_deep_empty('young_forest', 'cl2', 'cl2_vege_unr', 'value')
    # get_deep_empty('young_forest', 'cl3', 'cl3_seed_sur', 'value')
    # get_deep_empty('young_forest', 'cl3', 'cl3_seed_unr', 'value')
    # get_deep_empty('young_forest', 'cl3', 'cl3_vege_sur', 'value')
    # get_deep_empty('young_forest', 'cl3', 'cl3_vege_unr', 'value')
    # get_deep_empty('young_forest', 'cl4', 'cl4_seed_sur', 'value')
    # get_deep_empty('young_forest', 'cl4', 'cl4_seed_unr', 'value')
    # get_deep_empty('young_forest', 'cl4', 'cl4_vege_sur', 'value')
    # get_deep_empty('young_forest', 'cl4', 'cl4_vege_unr', 'value')
    # get_deep_empty('young_forest', 'cl4_height', 'cl4_seed_sur', 'value')
    # get_deep_empty('young_forest', 'cl4_height', 'cl4_seed_unr', 'value')
    # get_deep_empty('young_forest', 'cl4_height', 'cl4_vege_sur', 'value')
    # get_deep_empty('young_forest', 'cl4_height', 'cl4_vege_unr', 'value')


        


    get_nested_inventory('executors', 'executor_1', 'code')
    get_nested_inventory('executors', 'executor_2', 'code')
    get_nested_inventory('executors', 'executor_3', 'code')
    get_nested_inventory('coordinates', 'coordinates_x', 'value')
    get_nested_inventory('coordinates', 'coordinates_y', 'value')
    get_nested_inventory('used_fp_coordinates', 'x', 'value')
    get_nested_inventory('used_fp_coordinates', 'y', 'value')
    get_nested_inventory('measurment_of_a_border', 'distance', 'value')
    get_nested_inventory('measurment_of_a_border', 'azimuth_1', 'value')
    get_nested_inventory('measurment_of_a_border', 'azimuth_2', 'value')
    get_nested_inventory('measurment_of_a_border', 'azimuth_from_an_edge', 'value')
    get_nested_inventory('point_of_a_link_1', 'azimuth', 'value')
    get_nested_inventory('point_of_a_link_2', 'azimuth', 'value')
    get_nested_inventory('point_of_a_link_3', 'azimuth', 'value')
    get_nested_inventory('point_of_a_link_1', 'distance', 'value')
    get_nested_inventory('point_of_a_link_2', 'distance', 'value')
    get_nested_inventory('point_of_a_link_3', 'distance', 'value')
    get_nested_inventory('point_of_a_link_1', 'description', 'value')
    get_nested_inventory('point_of_a_link_2', 'description', 'value')
    get_nested_inventory('point_of_a_link_3', 'description', 'value')
    get_nested_inventory('slope', 'slope1', 'value')
    get_nested_inventory('slope', 'slope2', 'value')
    get_nested_inventory('impact_factors', 'snow_impact', 'code')
    get_nested_inventory('impact_factors', 'wind_impact', 'code')
    get_nested_inventory('impact_factors', 'landslide_impact', 'code')
    get_nested_inventory('impact_factors', 'rock_fall_impact', 'code')
    get_nested_inventory('impact_factors', 'avalanche_impact', 'code')
    get_nested_inventory('impact_factors', 'fire_impact', 'code')
    get_nested_inventory('impact_factors', 'grazing_impact', 'code')
    get_nested_inventory('impact_factors', 'wild_animal_impact', 'code')
    get_nested_inventory('impact_factors', 'anthropogenic_impact', 'code')
    get_nested_inventory('forest_resistance', 'strain', 'code')
    get_nested_inventory('forest_resistance', 'height_diameter', 'code')
    get_nested_inventory('forest_resistance', 'crown_length', 'code')
    get_nested_inventory('forest_resistance', 'crown_form', 'code')
    get_nested_inventory('forest_resistance', 'vertical_axis', 'code')
    get_nested_inventory('forest_resistance', 'roots', 'code')
    get_nested_inventory('forest_resistance', 'height', 'code')
    get_nested_inventory('forest_resistance', 'clearing', 'code')
    get_nested_inventory('forest_resistance', 'structure', 'code')
    get_nested_inventory('forest_resistance', 'sanitary_state', 'code')
    get_nested_inventory('area', 'area_x', 'value')
    get_nested_inventory('area', 'area_y', 'value')




    get_inventory('cycle', 'code')
    get_inventory('availability', 'code')
    get_inventory('inavailability_reason', 'value')
    get_inventory('landuse', 'code')
    get_inventory('not_a_forest_reason', 'value')
    get_inventory('gps', 'code')
    get_inventory('map_number', 'value')
    get_inventory('scale', 'code')
    get_inventory('deviation', 'value')
    get_inventory('height_map', 'value')
    get_inventory('height_gps', 'value')
    get_inventory('used_fixed_point_number', 'value')
    get_inventory('used_fixed_point_height_map', 'value')
    get_inventory('used_fixed_point_height_thommen', 'value')
    get_inventory('used_fp_description', 'value')
    get_inventory('borders', 'code')
    get_inventory('region', 'code')
    get_inventory('district', 'code')
    get_inventory('oblast', 'code')
    get_inventory('leshoz', 'code')
    get_inventory('forestry', 'code')
    get_inventory('block', 'value')
    get_inventory('stand', 'value')
    get_inventory('exposition', 'value')
    get_inventory('relief', 'code')
    get_inventory('microrelief', 'code')
    get_inventory('erosion', 'code')
    get_inventory('growth_location', 'code')
    get_inventory('forest_origin', 'code')
    get_inventory('evolution_stage', 'code')
    get_inventory('forest_kind', 'code')
    get_inventory('crown_density', 'code')
    get_inventory('main_species_part', 'code')
    get_inventory('layerage', 'code')
    get_inventory('underbrush', 'code')
    get_inventory('stability', 'code')
    get_inventory('pasture', 'code')
    get_inventory('grass_cover', 'value')
    get_inventory('outer_radius', 'value')
    get_inventory('inner_radius', 'value')
    get_inventory('young_forest_origin', 'code')
    # print(newDict)
   
    json_dict = json.dumps(newDict)
    # print(json_dict)

    """insert and select block_id"""
    block_data = (
        newDict['sample_plot_inventory']['forestry']['code'],
        newDict['sample_plot_inventory']['block']['value']
    )
    check_for_block_query = """SELECT gid from forest.block WHERE forestry_id = {} AND block_num = {}""".format(
        newDict['sample_plot_inventory']['forestry']['code'],
        newDict['sample_plot_inventory']['block']['value'])
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
    print('start')
    isBlock = cur.rowcount
    if isBlock == 0:
        cur.execute(insert_block_query, block_data)
        block_id = cur.fetchone()[0]
        print('block_id is ', block_id)
    else:
        cur.execute(check_for_block_query)
        block_id = cur.fetchone()[0]
        print('block_id is ', block_id)
    # print('isBlock is ', isBlock)

    conn.commit()
    cur.close()

    """ insert a values into the stand_test table """
   

    inv_data = (
        newDict['sample_plot_inventory']['trial_plot_number']['value'],
        0,
        newDict['sample_plot_inventory']['cycle']['code'],
        0,
        newDict['sample_plot_inventory']['leshoz']['code'],
        newDict['sample_plot_inventory']['@modified'],
        None,
        None,
        newDict['sample_plot_inventory']['group_number']['code'],
        newDict['sample_plot_inventory']['executors']['executor_1']['code'],
        newDict['sample_plot_inventory']['executors']['executor_2']['code'],
        newDict['sample_plot_inventory']['executors']['executor_3']['code'],
        None,
        newDict['sample_plot_inventory']['map_number']['value'],
        newDict['sample_plot_inventory']['scale']['code'],
        newDict['sample_plot_inventory']['deviation']['value'],
        newDict['sample_plot_inventory']['coordinates']['coordinates_x']['value'],
        newDict['sample_plot_inventory']['coordinates']['coordinates_y']['value'],
        newDict['sample_plot_inventory']['height_map']['value'],
        newDict['sample_plot_inventory']['height_gps']['value'],
        newDict['sample_plot_inventory']['used_fixed_point_number']['value'],
        newDict['sample_plot_inventory']['used_fp_coordinates']['x']['value'],
        newDict['sample_plot_inventory']['used_fp_coordinates']['y']['value'],
        newDict['sample_plot_inventory']['used_fixed_point_height_map']['value'],
        newDict['sample_plot_inventory']['used_fixed_point_height_thommen']['value'],
        newDict['sample_plot_inventory']['used_fp_description']['value'],
        newDict['sample_plot_inventory']['availability']['code'],
        newDict['sample_plot_inventory']['inavailability_reason']['value'],
        newDict['sample_plot_inventory']['landuse']['code'],
        newDict['sample_plot_inventory']['not_a_forest_reason']['value'],
        newDict['sample_plot_inventory']['borders']['code'],
        newDict['sample_plot_inventory']['measurment_of_a_border']['distance']['value'],
        newDict['sample_plot_inventory']['measurment_of_a_border']['azimuth_1']['value'],
        newDict['sample_plot_inventory']['measurment_of_a_border']['azimuth_2']['value'],
        newDict['sample_plot_inventory']['measurment_of_a_border']['azimuth_from_an_edge']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_1']['azimuth']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_2']['azimuth']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_3']['azimuth']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_1']['distance']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_2']['distance']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_3']['distance']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_1']['description']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_2']['description']['value'],
        newDict['sample_plot_inventory']['point_of_a_link_3']['description']['value'],
        newDict['sample_plot_inventory']['slope']['slope1']['value'],
        newDict['sample_plot_inventory']['slope']['slope2']['value'],
        newDict['sample_plot_inventory']['exposition']['value'],
        newDict['sample_plot_inventory']['relief']['code'],
        newDict['sample_plot_inventory']['microrelief']['code'],
        newDict['sample_plot_inventory']['erosion']['code'],
        newDict['sample_plot_inventory']['growth_location']['code'],
        newDict['sample_plot_inventory']['forest_origin']['code'],
        newDict['sample_plot_inventory']['evolution_stage']['code'],
        newDict['sample_plot_inventory']['forest_kind']['code'],
        newDict['sample_plot_inventory']['crown_density']['code'],
        newDict['sample_plot_inventory']['main_species_part']['code'],
        newDict['sample_plot_inventory']['layerage']['code'],
        newDict['sample_plot_inventory']['underbrush']['code'],
        newDict['sample_plot_inventory']['impact_factors']['snow_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['wind_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['landslide_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['rock_fall_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['avalanche_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['fire_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['grazing_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['wild_animal_impact']['code'],
        newDict['sample_plot_inventory']['impact_factors']['anthropogenic_impact']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['strain']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['height_diameter']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['crown_length']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['crown_form']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['vertical_axis']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['roots']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['height']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['clearing']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['structure']['code'],
        newDict['sample_plot_inventory']['forest_resistance']['sanitary_state']['code'],
        newDict['sample_plot_inventory']['area']['area_x']['value'],
        newDict['sample_plot_inventory']['area']['area_y']['value'],
        newDict['sample_plot_inventory']['stability']['code'],
        newDict['sample_plot_inventory']['pasture']['code'],
        newDict['sample_plot_inventory']['grass_cover']['value'],
        newDict['sample_plot_inventory']['outer_radius']['value'],
        newDict['sample_plot_inventory']['inner_radius']['value'],
        newDict['sample_plot_inventory']['young_forest_origin']['code'],
        newDict['sample_plot_inventory']['@modified'],
        newDict['sample_plot_inventory']['forestry']['code'],
        block_id,
        newDict['sample_plot_inventory']['stand']['value'],
        newDict['sample_plot_inventory']['gps']['code'],
        newDict['sample_plot_inventory']['job_start']['hour'],
        newDict['sample_plot_inventory']['job_complete']['hour'],
        newDict['sample_plot_inventory']['district']['code']
    )
    sql = """INSERT INTO inv.inventor (
        inventor_num,
        processed,
        cycle,
        year,
        leshoz_id,
        completion_date,
        workstart1,
        workend1,
        workgroup_num,
        executor1_id,
        executor2_id,
        executor3_id,
        geom,
        mapnumber,
        scale_id,
        deviation,
        trialplot_xl,
        trialplot_yl,
        trialplot_minh,
        trialplot_maxh,
        ufp_num,
        ufp_x,
        ufp_y,
        ufpmap_h,
        ufpthommen_h,
        ufpdescription,
        availability,
        inaccessibilityreason,
        landusetype_id,
        landusereason,
        border_flag,
        borderdist,
        borderazimuth_0,
        borderazimuth_1,
        borderazimuth_2,
        anchorazimuth_1,
        anchorazimuth_2,
        anchorazimuth_3,
        anchordist_1,
        anchordist_2,
        anchordist_3,
        anchordescript_1,
        anchordescript_2,
        anchordescript_3,
        slope_1,
        slope_2,
        exposition,
        relief_id,
        microrelief_id,
        erosion_id,
        growthlocation_id,
        forestorigin_id,
        evolutionstage_id,
        forestkind_id,
        crowndensity_id,
        mainspeciespart_id,
        layerage_id,
        underbrush_id,
        snowimpact_id,
        windimpact_id,
        landslideimpact_id,
        rockfallimpact_id,
        avalancheimpact_id,
        fireimpact_id,
        grazingimpact_id,
        wildanimalimpact_id,
        anthropogenimpact_id,
        weatherresistance_cl,
        hdresistance_cl,
        crownlenresistance_cl,
        crownformresistance_cl,
        vertaxisresistance_cl,
        rootresistance_cl,
        heightresistance_cl,
        clearingresistance_cl,
        structresistance_cl,
        sanitaryresistance_cl,
        square_x,
        square_y,
        trialplotstability_id,
        pasture_id,
        grasscover,
        outerradius,
        innerradius,
        youngforestorigin_id,
        modified,
        forestry_id,
        block_id,
        stand_id,
        gps_use,
        workstart,
        workend,
        raion_id
        )
        VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING inventor_id"""
    conn = None
    try:

        conn = psycopg2.connect(
            dbname=cr_dbname, user=cr_user, password=cr_password, host=cr_host)
        cur = conn.cursor()
        cur.execute(sql, inv_data)
        print('insert successsssss')
        newId = cur.fetchone()[0]
        print('newId is ', newId)
        modified = newDict['sample_plot_inventory']['@modified']
       
        polyline_counter = 0
        growth_info_counter = 0
        bush_species_counter = 0
        timber_counting_counter = 0
        young_forest_counter = 0


        if 'polyline' not in newDict['sample_plot_inventory'].keys():
            print('end?')
        else:
            try:
                a = newDict['sample_plot_inventory']['polyline'].keys()
                get_nested_inventory('polyline', 'point_number', 'value')
                get_nested_inventory('polyline', 'height', 'value')
                get_nested_inventory('polyline', 'azimuth', 'value')
                get_nested_inventory('polyline', 'distance_on_map', 'value')
                get_nested_inventory('polyline', 'distance_on_field', 'value')
                polyline = newDict['sample_plot_inventory']['polyline']
                insert_polyline(
                    polyline, newId, modified, polyline_counter)
            except:
                for polyline in newDict['sample_plot_inventory']['polyline']:
                    def get_polyline(arg1, arg2):
                        if arg1 not in polyline.keys():
                            polyline[arg1] = {arg2: None}
                        elif polyline[arg1] is None:
                            polyline[arg1] = {arg2: None}
                    get_polyline('point_number', 'value')
                    get_polyline('height', 'value')
                    get_polyline('azimuth', 'value')
                    get_polyline('distance_on_map', 'value')
                    get_polyline('distance_on_field', 'value')
                    # print('polyline is ', polyline)
                    
                    insert_polyline(
                    polyline, newId, modified, polyline_counter)
                    polyline_counter = polyline_counter + 1

        if 'growth_info' not in newDict['sample_plot_inventory'].keys():
            print('end?')
        else:
            try:
                a = newDict['sample_plot_inventory']['growth_info'].keys()
                print(a)

                get_nested_inventory('growth_info', 'tree_num', 'value')
                get_nested_inventory('growth_info', 'wood_species', 'code')
                get_nested_inventory('growth_info', 'diameter', 'value')
                get_nested_inventory('growth_info', 'ring_num', 'value')
                get_nested_inventory('growth_info', 'length', 'value')
                get_nested_inventory('growth_info', 'age', 'value')
                growth_info = newDict['sample_plot_inventory']['growth_info']
                insert_growth_info(
                    growth_info, newId, modified, growth_info_counter)
            except:
                print('hmmmmm ', newDict['sample_plot_inventory']['growth_info'])
                for growth_info in newDict['sample_plot_inventory']['growth_info']:
                    print('gr is ', growth_info)
                    def get_growth_info(arg1, arg2):
                        if arg1 not in growth_info.keys():
                            growth_info[arg1] = {arg2: None}
                        elif growth_info[arg1] is None:
                            growth_info[arg1] = {arg2: None}
                    get_growth_info('tree_num', 'value')
                    get_growth_info('wood_species', 'value')
                    get_growth_info('diameter', 'value')
                    get_growth_info('ring_num', 'value')
                    get_growth_info('length', 'value')
                    get_growth_info('age', 'value')
                    insert_growth_info(
                    growth_info, newId, modified, growth_info_counter)
                    growth_info_counter = growth_info_counter + 1
            

        if 'bush_species' not in newDict['sample_plot_inventory'].keys():
            print('end?')
        else:    
            try:
                a = newDict['sample_plot_inventory']['bush_species'].keys()
                get_nested_inventory('bush_species', 'bush_species', 'code')
                get_nested_inventory('bush_species', 'bush_height', 'value')
                bush_species = newDict['sample_plot_inventory']['bush_species']
                insert_bush_species(
                    bush_species, newId, modified, bush_species_counter)
            except:
                for bush_species in newDict['sample_plot_inventory']['bush_species']:
                    def get_bush_species(arg1, arg2):
                        if arg1 not in bush_species.keys():
                            bush_species[arg1] = {arg2: None}
                        elif bush_species[arg1] is None:
                            bush_species[arg1] = {arg2: None}
                    get_bush_species('bush_species', 'code')
                    get_bush_species('bush_height', 'value')
                    insert_bush_species(
                    bush_species, newId, modified, bush_species_counter)
                    bush_species_counter = bush_species_counter + 1

        

        if 'timber_counting' not in newDict['sample_plot_inventory'].keys():
            print('end?')
        else:
            try:

                a = newDict['sample_plot_inventory']['timber_counting'].keys()
                get_nested_inventory('timber_counting', 'tree_num', 'value')
                get_nested_inventory('timber_counting', 'azimuth', 'value')
                get_nested_inventory('timber_counting', 'distance', 'value')
                get_nested_inventory('timber_counting', 'wood_species', 'code')
                get_nested_inventory('timber_counting', 'diameter', 'value')
                get_nested_inventory('timber_counting', 'height', 'value')
                get_nested_inventory('timber_counting', 'tier', 'code')
                get_nested_inventory('timber_counting', 'tree_cl', 'code')
                get_nested_inventory('timber_counting', 'damage_place', 'code')
                get_nested_inventory('timber_counting', 'damage_reason', 'code')
                get_nested_inventory('timber_counting', 'market_length', 'code')
                get_nested_inventory('timber_counting', 'root_burl', 'code')
                get_nested_inventory('timber_counting', 'trunk_burl', 'code')
                get_nested_inventory('timber_counting', 'note', 'value')
                timber_counting = newDict['sample_plot_inventory']['timber_counting']
                insert_timber_counting(
                    timber_counting, newId, modified, timber_counting_counter)
            except:
                for timber_counting in newDict['sample_plot_inventory']['timber_counting']:
                    def get_timber_counting(arg1, arg2):
                        if arg1 not in timber_counting.keys():
                            timber_counting[arg1] = {arg2: None}
                        elif timber_counting[arg1] is None:
                            timber_counting[arg1] = {arg2: None}
                    get_timber_counting('tree_num', 'value')
                    get_timber_counting('azimuth', 'value')
                    get_timber_counting('distance', 'value')
                    get_timber_counting('wood_species', 'code')
                    get_timber_counting('diameter', 'value')
                    get_timber_counting('height', 'value')
                    get_timber_counting('tier', 'code')
                    get_timber_counting('tree_cl', 'code')
                    get_timber_counting('damage_place', 'code')
                    get_timber_counting('damage_reason', 'code')
                    get_timber_counting('market_length', 'code')
                    get_timber_counting('root_burl', 'code')
                    get_timber_counting('trunk_burl', 'code')
                    get_timber_counting('note', 'value')
                    insert_timber_counting(
                    growth_info, newId, modified, timber_counting_counter)
                    timber_counting_counter = timber_counting_counter + 1

        

        if 'young_forest' not in newDict['sample_plot_inventory'].keys():
            print('check')
        else:
            try:

                a = newDict['sample_plot_inventory']['young_forest'].keys()
                print(a)
                get_nested_inventory('young_forest', 'wood_species', 'code')
                get_deep_nested_inventory('young_forest', 'cl1', 'cl1_seed_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl1', 'cl1_seed_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl1', 'cl1_vege_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl1', 'cl1_vege_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl2', 'cl2_seed_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl2', 'cl2_seed_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl2', 'cl2_vege_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl2', 'cl2_vege_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl3', 'cl3_seed_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl3', 'cl3_seed_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl3', 'cl3_vege_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl3', 'cl3_vege_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl4', 'cl4_seed_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl4', 'cl4_seed_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl4', 'cl4_vege_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl4', 'cl4_vege_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl4_height', 'cl4_seed_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl4_height', 'cl4_seed_unr', 'value')
                get_deep_nested_inventory('young_forest', 'cl4_height', 'cl4_vege_sur', 'value')
                get_deep_nested_inventory('young_forest', 'cl4_height', 'cl4_vege_unr', 'value')

                
                young_forest = newDict['sample_plot_inventory']['young_forest']
                insert_young_forest(
                    young_forest, newId, modified, young_forest_counter)
            except:
                for young_forest in newDict['sample_plot_inventory']['young_forest']:
                    def get_young_forest(arg1, arg2, arg3):
                        try:
                            a = young_forest[arg1][arg2][arg3]
                        except:
                            young_forest[arg1][arg2] = {arg3: None}
                    
                    get_young_forest('cl1', 'cl1_seed_sur', 'value')

                    get_young_forest('cl1', 'cl1_seed_unr', 'value')
                    get_young_forest('cl1', 'cl1_vege_sur', 'value')
                    get_young_forest('cl1', 'cl1_vege_unr', 'value')
                    get_young_forest('cl2', 'cl2_seed_sur', 'value')
                    get_young_forest('cl2', 'cl2_seed_unr', 'value')
                    get_young_forest('cl2', 'cl2_vege_sur', 'value')
                    get_young_forest('cl2', 'cl2_vege_unr', 'value')
                    get_young_forest('cl3', 'cl3_seed_sur', 'value')
                    get_young_forest('cl3', 'cl3_seed_unr', 'value')
                    get_young_forest('cl3', 'cl3_vege_sur', 'value')
                    get_young_forest('cl3', 'cl3_vege_unr', 'value')
                    get_young_forest('cl4', 'cl4_seed_sur', 'value')
                    get_young_forest('cl4', 'cl4_seed_unr', 'value')
                    get_young_forest('cl4', 'cl4_vege_sur', 'value')
                    get_young_forest('cl4', 'cl4_vege_unr', 'value')
                    get_young_forest('cl4_height', 'cl4_seed_sur', 'value')
                    get_young_forest('cl4_height', 'cl4_seed_unr', 'value')
                    get_young_forest('cl4_height', 'cl4_vege_sur', 'value')
                    get_young_forest('cl4_height', 'cl4_vege_unr', 'value')
                    print(young_forest)
                    insert_young_forest(
                    young_forest, newId, modified, young_forest_counter)
                    young_forest_counter = young_forest_counter + 1


                
        # insert_action1(newDict, newId, modified, action_counter)
        # insert_action1_tillage(newDict, newId, modified)
        # insert_action1_creation(newDict, newId, modified)
        # insert_polygon(newDict, stand_code_str, forestry_num, block_id)
        conn.commit()
        cur.close()
        print('sss')

        # update_forestry_num(newDict, newId)

        # print(newId)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
