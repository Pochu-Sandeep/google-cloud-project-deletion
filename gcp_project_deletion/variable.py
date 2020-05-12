import sys

from google.oauth2 import service_account

from googleapiclient import discovery

from google.cloud import storage

#credentials = service_account.Credentials.from_service_account_file(sys.argv[1])

credentials = service_account.Credentials.from_service_account_file("//home/sandeep_pochu/sap-coe-devops-test.json")

service = discovery.build('compute', 'v1', credentials=credentials)

resource_manager_service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

service_usage_service = discovery.build('serviceusage', 'v1', credentials=credentials)

#storage_client = storage.Client.from_service_account_json(sys.argv[1])

storage_client = storage.Client.from_service_account_json("/home/sandeep_pochu/sap-coe-devops-test.json")
