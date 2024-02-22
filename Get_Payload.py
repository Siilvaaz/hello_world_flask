from google.cloud import storage

# Define your GCS bucket name
bucket_name = "pocjenkins"

# Define the names of the input and expected output payload files
input_payload_file = "input.json"
expected_output_payload_file = "expected_output.json"

# Define the local directory where you want to store the payload files
local_directory = "~"

# Function to download a file from GCS
def download_file_from_gcs(source_blob_name, destination_file_name):
    """Downloads a file from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"File {source_blob_name} downloaded to {destination_file_name}.")

if __name__ == "__main__":
    # Download the input payload file from GCS
    download_file_from_gcs(input_payload_file, local_directory + input_payload_file)

    # Download the expected output payload file from GCS
    download_file_from_gcs(expected_output_payload_file, local_directory + expected_output_payload_file)
