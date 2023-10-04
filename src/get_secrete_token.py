from google.cloud import secretmanager
from google.cloud import bigquery
from google.oauth2 import service_account



key_path = 'C:/Users/foodpanda_di/Documents/keys/di-th-auto-253de33a30ba.json'

credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/cloud-platform"],
    )

client = secretmanager.SecretManagerServiceClient(credentials=credentials)

def get_secret_data():
    secret_detail = "projects/234879409305/secrets/line_messaging_api_key_rider/versions/latest"
    response = client.access_secret_version(request={"name": secret_detail})
    data = response.payload.data.decode("UTF-8")
    return data


if __name__ == "__main__":
    value = get_secret_data()
    print(value)
