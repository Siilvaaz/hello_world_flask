# Verify_Payload.py

import json

def verify_payload(expected_output_file, received_output_file):
    with open(expected_output_file, 'r') as f:
        expected_output = json.load(f)
    with open(received_output_file, 'r') as f:
        received_output = json.load(f)
    
    if expected_output == received_output:
        print("Payloads match! Test case passed.")
    else:
        print("Payloads do not match! Test case failed.")

if __name__ == '__main__':
    expected_output_file = 'expected_output.json'
    received_output_file = 'received_payload.json'
    verify_payload(expected_output_file, received_output_file)
