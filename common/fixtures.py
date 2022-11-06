import pytest

first_census_entry = {
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

second_census_entry = {
    "age": 30,
    "workclass": "Private",
    "fnlgt": 1234,
    "education": "Bachelors",
    "education-num": 20,
    "marital-status": "Divorced",
    "occupation": "Armed-Forces",
    "relationship": "Husband",
    "race": "Black",
    "sex": "Male",
    "capital-gain": 20000,
    "capital-loss": 0,
    "hours-per-week": 50,
    "native-country": "England"
}

wrong_category_entry = {
    "age": 30,
    "workclass": "Worker",
    "fnlgt": 1234,
    "education": "Elementary",
    "education-num": 20,
    "marital-status": "Polyamorous",
    "occupation": "Rogue",
    "relationship": "Complicated",
    "race": "Pink",
    "sex": "Bacteria",
    "capital-gain": 20000,
    "capital-loss": 0,
    "hours-per-week": 50,
    "native-country": "Battania"
}

empty_entry = {
}

missing_fields_entry = {
    "age": 30,
    "workclass": "Private",
    "education": "Bachelors",
    "education-num": 20,
    "marital-status": "Dicorced",
    "relationship": "Husband",
    "sex": "Male",
    "capital-gain": 20000,
    "hours-per-week": 50,
    "native-country": "England"
}


@pytest.fixture
def census_entries():
    return [first_census_entry, second_census_entry]


@pytest.fixture
def wrong_census_entries():
    return [empty_entry, missing_fields_entry, wrong_category_entry]