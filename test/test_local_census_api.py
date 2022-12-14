import requests
from common.fixtures import census_entries, wrong_census_entries, generate_entries
import pytest
import os

from common.fixtures import generate_entry


@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_welcome():
    response = requests.get('http://127.0.0.1:8000/')
    assert response.status_code == 200
    result_call = response.json()
    assert "welcome" in result_call["result"].lower()


@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict_right(census_entries):
    for census_entry in census_entries:
        response = requests.post('http://127.0.0.1:8000/predict', json=census_entry)
        assert response.status_code == 200
        result_call = response.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict_wrong(wrong_census_entries):
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

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_print_out_wrong(wrong_census_entries):
    for census_entry in wrong_census_entries:
        response = requests.post('http://127.0.0.1:8000/print_out', json=census_entry)
        assert response.status_code != 200

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_printout_random(generate_entries):
    for generated_entry in generate_entries:
        print(generated_entry)
        response = requests.post('http://127.0.0.1:8000/print_out', json=generated_entry)
        print(response.content)
        assert response.status_code == 200
        result_call = response.json()
        assert "age" in result_call

@pytest.mark.skipif(os.environ.get("TEST_LOCAL_API") == None, reason="TEST_LOCAL_API not defined")
def test_predict_random(generate_entries):
    for generated_entry in generate_entries:
        print(generated_entry)
        response = requests.post('http://127.0.0.1:8000/predict', json=generated_entry)
        print(response.content)
        assert response.status_code == 200
        result_call = response.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]
