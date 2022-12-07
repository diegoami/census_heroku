import pytest
import requests
import os

from common.fixtures import census_entries, wrong_census_entries, generate_entries
from common.fixtures import generate_entry

@pytest.fixture
def host():
    return os.environ.get("HOST", "localhost")

@pytest.fixture
def port():
    return os.environ.get("PORT", 80)


@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_predict(census_entries, host, port):
    for census_entry in census_entries:
        response = requests.post(f'http://{host}:{port}/predict', json=census_entry)
        print(response.status_code)
        print(response.json())

@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_predict_right(census_entries, host, port):
    for census_entry in census_entries:
        response = requests.post(f'http://{host}:{port}/predict', json=census_entry)
        assert response.status_code == 200
        result_call = response.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]

@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_predict_wrong(wrong_census_entries, host, port):
    for census_entry in wrong_census_entries:
        response = requests.post(f'http://{host}:{port}/predict', json=census_entry)
        assert response.status_code != 200

@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_print_out(census_entries, host, port):
    for census_entry in census_entries:
        response = requests.post(f'http://{host}:{port}/print_out', json=census_entry)
        assert response.status_code == 200
        result_call = response.json()
        assert "age" in result_call

@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_print_out_wrong(wrong_census_entries, host, port):
    for census_entry in wrong_census_entries:
        response = requests.post(f'http://{host}:{port}/print_out', json=census_entry)
        assert response.status_code != 200


@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_printout_random(generate_entries, host, port):
    for generated_entry in generate_entries:
        print(generated_entry)
        response = requests.post(f'http://{host}:{port}/print_out', json=generated_entry)
        print(response.content)
        assert response.status_code == 200
        result_call = response.json()
        assert "age" in result_call

@pytest.mark.skipif(os.environ.get("TEST_REMOTE_API") == None, reason="TEST_REMOTE_API not defined")
def test_predict_random(generate_entries, host, port):
    for generated_entry in generate_entries:
        print(generated_entry)
        response = requests.post(f'http://{host}:{port}/predict', json=generated_entry)
        print(response.content)
        assert response.status_code == 200
        result_call = response.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]
