import requests

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


def test_predict():
    response = requests.post('https://pacific-garden-34952.herokuapp.com/predict', json=dummy_census_entry)

    print(response.status_code)
    print(response.json())