import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_rider_credential
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.country_TH_logistics_line_rider_credential_request"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = False
url = "https://api.line.me/v2/bot/message/push"

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
      SELECT DISTINCT
        NULL AS vendor_code,
        rider_id,
        line_user_id,
        rider_email,
        rider_password
      FROM {query_table}
      WHERE DATE(record_created_at_local) = CURRENT_DATE
      LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT DISTINCT
        NULL AS vendor_code,
        rider_id,
        line_user_id,
        rider_email,
        rider_password
      FROM {query_table}
      WHERE DATE(record_created_at_local) = CURRENT_DATE
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_rider_credential_request*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")

try:
  reponse_code_list, json_list = send_request_line_api_rider_credential(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_rider_credential_request*: Failed send API request: ' + str(e)})
  # print(e)

df = dataframe.filter(items=['vendor_code', 'line_user_id'])
df["return_response"] = reponse_code_list
df["msg_sent_date_time"] = now
df["template_id_if_any"] = "line_rider_credential_request"
df["msg_url"] = url
df["msg_content"] = 'content rider_id: ' + dataframe['rider_id'] \
                    + ',' + 'content rider_email: ' + dataframe['rider_email']
df_records = df.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_rider_credential_request*: Failed to record logs: ' + str(e)})
  # print(e)
