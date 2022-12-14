import json
from fastapi.testclient import TestClient
from common.fixtures import generate_entry, census_entries, wrong_census_entries


from api.main import app

client = TestClient(app)


def test_get(census_entries):
    r = client.get("/")
    assert r.status_code == 200
    result_call = r.json()["result"]
    assert "Welcome" in result_call

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

def test_generate_entries():
    results = [0, 0]
    for i in range(100):
        gen_entry = generate_entry()
        r = client.post("/predict", json=gen_entry)
        result_call = r.json()
        pred = result_call["result"].lower()
        if pred == ">50k":
            results[1] += 1
        elif pred == "<=50k":
            results[0] += 1
        else:
            print(pred)
    assert results[0] + results[1] == 100
    assert results[1] < results[0]
