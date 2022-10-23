import requests

from common.fixtures import census_entries



def test_predict(census_entries):
    for census_entry in census_entries:
        response = requests.post('https://pacific-garden-34952.herokuapp.com/predict', json=census_entry)
        print(response.status_code)
        print(response.json())