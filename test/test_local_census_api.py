import requests
from common.fixtures import census_entries, wrong_census_entries
import pytest
import os

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict_right(census_entries):
    for census_entry in census_entries:
        response = requests.post('http://127.0.0.1:8000/predict', json=census_entry)
        assert response.status_code == 200
        result_call = response.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict_wrong(census_entries):
    for census_entry in wrong_census_entries:
        response = requests.post('http://127.0.0.1:8000/predict', json=census_entry)
        assert response.status_code != 200

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_print_out(census_entries):
    for census_entry in census_entries:
        response = requests.post('http://127.0.0.1:8000/print_out', json=census_entry)
        assert response.status_code == 200
        result_call = response.json()
        assert "age" in result_call
