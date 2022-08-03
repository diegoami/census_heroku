import json
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

dummy_census_entry = {
    "age": 20,
    "workclass": "State-gov",
    "fnlgt": 3000,
    "education": "Doctorate",
    "education-num": 20,
    "marital-status": "Never-married",
    "occupation": "Sales",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital-gain": 10000,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}



def test_print_out():
    r = client.post("/print_out", json=dummy_census_entry)
    result_call = r.json()
    assert (result_call == dummy_census_entry)


def test_predict():
    r = client.post("/predict", json=dummy_census_entry)
    result_call = r.json()
    assert result_call["result"].lower() in ["<=50k", ">50k"]
