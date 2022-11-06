import requests
from common.fixtures import census_entries
import pytest
import os

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict(census_entries):
    for census_entry in census_entries:
        response = requests.post('http://127.0.0.1:8000/predict', json=census_entry)
        print(response.status_code)
        print(response.json())