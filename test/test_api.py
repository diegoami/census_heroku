import json
from fastapi.testclient import TestClient
from common.fixtures import census_entries, wrong_census_entries


from api.main import app

client = TestClient(app)



def test_print_out(census_entries):
    for census_entry in census_entries:
        r = client.post("/print_out", json=census_entry)
        result_call = r.json()
        assert "age" in result_call

def test_predict_right(census_entries):
    for census_entry in census_entries:
        r = client.post("/predict", json=census_entry)
        assert r.status_code == 200
        result_call = r.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]

def test_predict_wrong(wrong_census_entries):
    for wrong_census_entry in wrong_census_entries:
        r = client.post("/predict", json=wrong_census_entry)
        assert r.status_code != 200
