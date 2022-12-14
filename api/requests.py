import requests
import json

def do_call(host, port, entry):
    print(" ================ CALL ====================")
    print(f"ENTRY: {json.dumps(entry)}")
    response = requests.post(f'http://{host}:{port}/predict', json=entry)
    result_status_code = response.status_code
    print(f"STATUS CODE: {result_status_code}")
    result_call = response.json()
    print(f"RESULT: {result_call}")

