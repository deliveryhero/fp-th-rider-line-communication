import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v3
from get_secrete_token import get_secret_data
import datetime, pytz
from template import json_object
import requests


# Basic configuration tables
slack_webhook = os.getenv('slack_webhook')
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_incubation_weekly_report"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
Live = True
url = "https://api.line.me/v2/bot/message/push"
json_data = json_object
token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT
      vendor_code,
      vendor_name,
      'U2b9495e231b925da2ed4163beeef6dad' AS LineUserID,
      CAST(ihs_score AS STRING) AS ihs_score,
      CAST(customers AS STRING) AS customers,
      IF(
        perc_customer_growth > 0.00,
        CONCAT("🔼", perc_customer_growth),
        CONCAT("🔽", perc_customer_growth)
      ) AS perc_customer_growth,
      CAST(valid_orders AS STRING) AS valid_orders,
      IF(
        perc_order_growth > 0.00,
        CONCAT("🔼", perc_order_growth),
        CONCAT("🔽", perc_order_growth)
      ) AS perc_order_growth,
      top1_best_seller,
      top2_best_seller,
      top3_best_seller,
      CAST(failed_orders AS STRING) AS failed_orders,
      improve_order,
      top_failed_product,
      improve_menu,
      top_failed_reason,
      improve_top_failed_reason,
      perc_offline,
      top_offline_reason,
      improve_top_offline_reason,
      CAST(first_date AS STRING) AS first_date,
      CAST(last_date AS STRING) AS last_date
    FROM {query_table}
    WHERE vendor_code != 'a0j1'
    LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT
        vendor_code,
        vendor_name,
        line_user_id AS LineUserID,
        CAST(ihs_score AS STRING) AS ihs_score,
        CAST(customers AS STRING) AS customers,
        IF(
          perc_customer_growth > 0.00,
          CONCAT("🔼", perc_customer_growth),
          CONCAT("🔽", perc_customer_growth)
        ) AS perc_customer_growth,
        CAST(valid_orders AS STRING) AS valid_orders,
        IF(
          perc_order_growth > 0.00,
          CONCAT("🔼", perc_order_growth),
          CONCAT("🔽", perc_order_growth)
        ) AS perc_order_growth,
        top1_best_seller,
        top2_best_seller,
        top3_best_seller,
        CAST(failed_orders AS STRING) AS failed_orders,
        improve_order,
        top_failed_product,
        improve_menu,
        top_failed_reason,
        improve_top_failed_reason,
        perc_offline,
        top_offline_reason,
        improve_top_offline_reason,
        CAST(first_date AS STRING) AS first_date,
        CAST(last_date AS STRING) AS last_date
      FROM {query_table}
    """
try:
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*Incubation_weekly_report*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_v3(url = url, headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*Incubation_weekly_report*: Failed send API request: ' + str(e)})

try:
  dataframe = dataframe.filter(items=['vendor_code', 'LineUserID'])
  dataframe.rename(columns={'LineUserID': 'line_user_id'}, inplace=True)
  dataframe["return_response"] = reponse_code_list
  dataframe["msg_sent_date_time"] = now
  dataframe["template_id_if_any"] = "Incubation_weekly_report"
  dataframe["msg_url"] = url
  dataframe["msg_content"] = json_list
  df_records = dataframe.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*Incubation_weekly_report*: Failed to record logs: ' + str(e)})