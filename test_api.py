import json
from fastapi.testclient import TestClient
from common.fixtures import census_entries


from main import app

client = TestClient(app)



def test_print_out(census_entries):
    for census_entry in census_entries:
        r = client.post("/print_out", json=census_entry)
        result_call = r.json()
        assert (result_call == census_entry)


def test_predict(census_entries):
    for census_entry in census_entries:
        r = client.post("/predict", json=census_entry)
        result_call = r.json()
        assert result_call["result"].lower() in ["<=50k", ">50k"]
