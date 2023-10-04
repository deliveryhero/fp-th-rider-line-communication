import requests
import datetime
import json
import re

def send_request_line_api(url, headers, json, list):
    reponse_code_list = []
    url_list = []
    for i in list:
        user_specific_url = url.replace("user_id_variable", i)
        headers = headers
        json = json
        r = requests.post(user_specific_url, headers = headers, json = json)
        reponse_code = r.status_code
        reponse = r.json()
        reponse_code_list.append(reponse_code)
        url_list.append(user_specific_url)
    return reponse_code_list, url_list

def send_request_line_api_v2(url, headers, json_data, list):
    reponse_code_list = []
    json_list = []
    for i in list:
        user_specific_url = url
        headers = headers
        json_data['to'] = i
        json = json_data
        r = requests.post(user_specific_url, headers = headers, json = json)
        reponse_code = r.status_code
        reponse = r.json()
        print(reponse)
        reponse_code_list.append(reponse_code)
        json_list_data = str(json)
        json_list.append(json_list_data)
    return reponse_code_list, json_list

def send_request_line_api_v3(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{LineUserID}', row['LineUserID']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{vendor_code}', row['vendor_code']) \
                                .replace('{ihs_score}', row['ihs_score']) \
                                .replace('{customers}', row['customers']) \
                                .replace('{perc_customer_growth}', row['perc_customer_growth']) \
                                .replace('{valid_orders}', row['valid_orders']) \
                                .replace('{perc_order_growth}', row['perc_order_growth']) \
                                .replace('{top1_best_seller}', row['top1_best_seller']) \
                                .replace('{top2_best_seller}', row['top2_best_seller']) \
                                .replace('{top3_best_seller}', row['top3_best_seller']) \
                                .replace('{failed_orders}', row['failed_orders']) \
                                .replace('{improve_order}', row['improve_order']) \
                                .replace('{top_failed_product}', row['top_failed_product']) \
                                .replace('{improve_menu}', row['improve_menu']) \
                                .replace('{top_failed_reason}', row['top_failed_reason']) \
                                .replace('{improve_top_failed_reason}', row['improve_top_failed_reason']) \
                                .replace('{perc_offline}', row['perc_offline']) \
                                .replace('{top_offline_reason}', row['top_offline_reason']) \
                                .replace('{improve_top_offline_reason}', row['improve_top_offline_reason']) \
                                .replace('{first_date}', row['first_date']) \
                                .replace('{last_date}', row['last_date'])

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'LineUserID: ' + row['LineUserID'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'vendor_code: '+ row['vendor_code'] + ", " +
                        'ihs_score: '+ row['ihs_score'] + ", " +
                        'customers: '+ row['customers'] + ", " +
                        'perc_customer_growth: '+ row['perc_customer_growth'] + ", " +
                        'valid_orders: '+ row['valid_orders'] + ", " +
                        'perc_order_growth: '+ row['perc_order_growth'] + ", " +
                        'top1_best_seller: '+ row['top1_best_seller'] + ", " +
                        'top2_best_seller: '+ row['top2_best_seller'] + ", " +
                        'top3_best_seller: '+ row['top3_best_seller'] + ", " +
                        'failed_orders: '+ row['failed_orders'] + ", " +
                        'improve_order: '+ row['improve_order'] + ", " +
                        'top_failed_product: '+ row['top_failed_product'] + ", " +
                        'improve_menu: '+ row['improve_menu'] + ", " +
                        'top_failed_reason: '+ row['top_failed_reason'] + ", " +
                        'improve_top_failed_reason: '+ row['improve_top_failed_reason'] + ", " +
                        'perc_offline: '+ row['perc_offline'] + ", " +
                        'top_offline_reason: '+ row['top_offline_reason'] + ", " +
                        'improve_top_offline_reason: '+ row['improve_top_offline_reason'] + ", " +
                        'first_date: '+ row['first_date'] + ", " +
                        'last_date: '+ row['last_date']+'}')
    return reponse_code_list, json_list

def send_request_line_api_v4(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{line_user_id}', row['line_user_id']) \
                                .replace('{sum_check_in_required_mins}', row['sum_check_in_required_mins'])

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        print(r.text)
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append(json_data_v1)
    return reponse_code_list, json_list

def send_request_line_api_v5(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{line_user_id}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{start_date_in_thai}', row['start_date_in_thai']) \
                                .replace('{end_date_in_thai}', row['end_date_in_thai']) \
                                .replace('{total_offline_hours}', row['total_offline_hours']) \
                                .replace('{potential_order_loss}', row['potential_order_loss'])

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        print(r.text)
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append(json_data_v1)
    return reponse_code_list, json_list

def send_request_line_api_v6(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{line_user_id}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{start_date_in_thai}', row['start_date_in_thai']) \
                                .replace('{end_date_in_thai}', row['end_date_in_thai']) \
                                .replace('{total_offline_hours}', row['total_offline_hours'])

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        print(r.text)
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append(json_data_v1)
    return reponse_code_list, json_list

def send_request_line_api_insight_search_term(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{lineuserid}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{zone_name}', row['zone_name']) \
                                .replace('{custome_1}', row['serch_term_1']) \
                                .replace('{custome_2}', row['serch_term_2']) \
                                .replace('{custome_3}', row['serch_term_3']) \
                                .replace('{custome_4}', row['serch_term_4']) \
                                .replace('{custome_5}', row['serch_term_5']) 


        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'line_user_id: ' + row['line_user_id'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'zone_name: '+ row['zone_name'] + ", " +
                        'custome_1: '+ row['serch_term_1'] + ", " +
                        'custome_2: '+ row['serch_term_2'] + ", " +
                        'custome_3: '+ row['serch_term_3'] + ", " +
                        'custome_4: '+ row['serch_term_4'] + ", " +
                        'custome_5: '+ row['serch_term_5'] + '}')
    return reponse_code_list, json_list

def send_request_line_api_insight_top_5_best_selling(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{lineuserid}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{zone_name}', row['zone_name']) \
                                .replace('{menu1}', row['menu1']) \
                                .replace('{menu1_percent}', str(row['menu1_percent'])) \
                                .replace('{menu2}', row['menu2']) \
                                .replace('{menu2_percent}', str(row['menu2_percent'])) \
                                .replace('{menu3}', row['menu3']) \
                                .replace('{menu3_percent}', str(row['menu3_percent'])) \
                                .replace('{menu4}', row['menu4']) \
                                .replace('{menu4_percent}', str(row['menu4_percent'])) \
                                .replace('{menu5}', row['menu5']) \
                                .replace('{menu5_percent}', str(row['menu5_percent'])) 

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'line_user_id: ' + row['line_user_id'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'zone_name: '+ row['zone_name'] + ", " +
                        'menu1: '+ row['menu1'] + ", " +
                        'menu1_percent: '+ str(row['menu1_percent']) + ", " +
                        'menu2: '+ row['menu2'] + ", " +
                        'menu2_percent: '+ str(row['menu2_percent']) + ", " +
                        'menu3: '+ row['menu3'] + ", " +
                        'menu3_percent: '+ str(row['menu3_percent']) + ", " +
                        'menu4: '+ row['menu4'] + ", " +
                        'menu4_percent: '+ str(row['menu4_percent']) + ", " +
                        'menu5: '+ row['menu5'] + ", " +
                        'menu5_percent: '+ str(row['menu5_percent']) + '}')
    return reponse_code_list, json_list

def send_request_line_api_insight_basket_size(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{lineuserid}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{zone_name}', row['zone_name']) \
                                .replace('{custome_Zone_1}', str(row['zone_0_100'])) \
                                .replace('{custome_1}', str(row['vendor_0_100'])) \
                                .replace('{custome_Zone_2}', str(row['zone_101_200'])) \
                                .replace('{custome_2}', str(row['vendor_101_200'])) \
                                .replace('{custome_Zone_3}', str(row['zone_201_300'])) \
                                .replace('{custome_3}', str(row['vendor_201_300'])) \
                                .replace('{custome_Zone_4}', str(row['zone_301_400'])) \
                                .replace('{custome_4}', str(row['vendor_301_400'])) \
                                .replace('{custome_Zone_5}', str(row['zone_401'])) \
                                .replace('{custome_5}', str(row['vendor_401'])) 

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'line_user_id: ' + row['line_user_id'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'zone_name: '+ row['zone_name'] + ", " +
                        'custome_zone_1: '+ str(row['zone_0_100']) + ", " +
                        'custome_ven_1: '+ str(row['vendor_0_100']) + ", " +
                        'custome_zone_2: '+ str(row['zone_101_200']) + ", " +
                        'custome_ven_2: '+ str(row['vendor_101_200']) + ", " +
                        'custome_zone_3: '+ str(row['zone_201_300']) + ", " +
                        'custome_ven_3: '+ str(row['vendor_201_300']) + ", " +
                        'custome_zone_4: '+ str(row['zone_301_400']) + ", " +
                        'custome_ven_4: '+ str(row['vendor_301_400']) + ", " +
                        'custome_zone_5: '+ str(row['zone_401']) + ", " +
                        'custome_ven_5: '+ str(row['vendor_401']) + '}')
    return reponse_code_list, json_list

def send_request_line_api_insight_opening_time(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{lineuserid}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{zone_name}', row['zone_name']) \
                                .replace('{custome_11}', str(row['zone_5AM_10AM'])) \
                                .replace('{custome_1}', str(row['vendor_5AM_10AM'])) \
                                .replace('{custome_22}', str(row['zone_10AM_2PM'])) \
                                .replace('{custome_2}', str(row['vendor_10AM_2PM'])) \
                                .replace('{custome_33}', str(row['zone_2PM_5PM'])) \
                                .replace('{custome_3}', str(row['vendor_2PM_5PM'])) \
                                .replace('{custome_44}', str(row['zone_5PM_10PM'])) \
                                .replace('{custome_4}', str(row['vendor_5PM_10PM'])) \
                                .replace('{custome_55}', str(row['zone_10PM_5AM'])) \
                                .replace('{custome_5}', str(row['vendor_10PM_5AM'])) 

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'line_user_id: ' + row['line_user_id'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'zone_name: '+ row['zone_name'] + ", " +
                        'custom_zone_1: '+ str(row['zone_5AM_10AM']) + ", " +
                        'custom_ven_1: '+ str(row['vendor_5AM_10AM']) + ", " +
                        'custom_zone_2: '+ str(row['zone_10AM_2PM']) + ", " +
                        'custom_ven_2: '+ str(row['vendor_10AM_2PM']) + ", " +
                        'custom_zone_3: '+ str(row['zone_2PM_5PM']) + ", " +
                        'custom_ven_3: '+ str(row['vendor_2PM_5PM']) + ", " +
                        'custom_zone_4: '+ str(row['zone_5PM_10PM']) + ", " +
                        'custom_ven_4: '+ str(row['vendor_5PM_10PM']) + ", " +
                        'custom_zone_5: '+ str(row['zone_10PM_5AM']) + ", " +
                        'custom_ven_5: '+ str(row['vendor_10PM_5AM']) + '}')
    return reponse_code_list, json_list

def send_request_line_api_insight_top_3_and_ractors(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{lineuserid}', row['line_user_id']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{zone_name}', row['zone_name']) \
                                .replace('{cuisine_type}', row['cuisine_type']) \
                                .replace('{custom_1}', str(row['top_vendor_name_1'])) \
                                .replace('{custom_2}', str(row['top_vendor_name_2'])) \
                                .replace('{custom_3}', str(row['top_vendor_name_3'])) \
                                .replace('{top_dld}', str(row['zone_perc_dld'])) \
                                .replace('{vd_dld}', str(row['vendor_perc_dld'])) \
                                .replace('{top_dlp}', str(row['zone_perc_dlp'])) \
                                .replace('{vd_dlp}', str(row['vendor_perc_dlp'])) \
                                .replace('{top_failed_rate}', str(row['zone_perc_failed_rate'])) \
                                .replace('{vd_failed_rate}', str(row['vendor_perc_failed_rate'])) \
                                .replace('{top_offline}', str(row['zone_off_pct'])) \
                                .replace('{vd_offline}', str(row['vendor_off_pct'])) \
                                .replace('{top_rating}', str(row['zone_rating'])) \
                                .replace('{vd_rating}', str(row['vendor_rating'])) 

        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append('{'+'line_user_id: ' + row['line_user_id'] + ", " +
				        'vendor_name: ' + row['vendor_name'] + ", " +
                        'zone_name: '+ row['zone_name'] + ", " +
                        'cuisine_type: '+ str(row['cuisine_type']) + ", " +
                        'top_vendor_name_1: '+ str(row['top_vendor_name_1']) + ", " +
                        'top_vendor_name_2: '+ str(row['top_vendor_name_2']) + ", " +
                        'top_vendor_name_3: '+ str(row['top_vendor_name_3']) + ", " +
                        'zone_perc_dld: '+ str(row['zone_perc_dld']) + ", " +
                        'vendor_perc_dld: '+ str(row['vendor_perc_dld']) + ", " +
                        'zone_perc_dlp: '+ str(row['zone_perc_dlp']) + ", " +
                        'vendor_perc_dlp: '+ str(row['vendor_perc_dlp']) + ", " +
                        'zone_perc_failed_rate: '+ str(row['zone_perc_failed_rate']) + ", " +
                        'vendor_perc_failed_rate: '+ str(row['vendor_perc_failed_rate']) + ", " +
                        'zone_off_pct: '+ str(row['zone_off_pct']) + ", " +
                        'vendor_off_pct: '+ str(row['vendor_off_pct']) + ", " +
                        'zone_rating: '+ str(row['zone_rating']) + ", " +
                        'vendor_rating: '+ str(row['vendor_rating']) + '}')
    return reponse_code_list, json_list

def send_request_line_rich_menu_segment_messages(*args, **kwargs):
    url_list = kwargs['url']
    headers = kwargs['headers']
    reponse_code_list = []
    json = {}
    for i in url_list:
        print(i)
        r = requests.post(i, headers = headers, json = json)
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
    return reponse_code_list

def send_request_line_api_generic_reminder(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []

    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="--", inplace=True)
    df = df.reset_index()
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{line_user_id}', row['line_user_id'])
        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        print(r.text)
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append(json_data_v1)
    return reponse_code_list, json_list