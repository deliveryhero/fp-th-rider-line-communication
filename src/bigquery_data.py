from google.cloud import bigquery
from google.oauth2 import service_account

key_path = 'C:/Users/foodpanda_di/Documents/keys/di-th-auto-253de33a30ba.json'

credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/cloud-platform"],
    )

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def query_BQ_table(query):
    job_config_query = bigquery.QueryJobConfig()
    return client.query(query, job_config=job_config_query).to_dataframe()

def record_line_communication_logs(table_id, rows_to_insert):
    status = []
    for i in batch(rows_to_insert, 100):
        errors = client.insert_rows_json(table_id, i)
        if errors == []:
            status.append("New rows have been added.")
        else:
            status.append("Encountered errors while inserting rows: {}".format(errors))
    return status

def insert_line_statistical_data(data, table):
    return client.insert_rows_json(table, data)


    
