# Get_Payload.py

import os
from google.cloud import storage

def download_payload(project_id, bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def main(project_id, bucket_name, source_blob_name, destination_file_name):
    download_payload(project_id, bucket_name, source_blob_name, destination_file_name)

if __name__ == '__main__':
    project_id = 'sandbox-anthos'
    bucket_name = 'pocjenkins'
    source_blob_name = 'input.json'
    destination_file_name = 'input.json'
    main(project_id, bucket_name, source_blob_name, destination_file_name)
