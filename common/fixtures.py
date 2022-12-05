import pytest
import random

import numpy as np
random_nums = np.random.normal(loc=550, scale=30, size=1000)
from values.census_entry import WORKCLASSES, EDUCATIONS, MARITAL_STATUSES, OCCUPATIONS, RELATIONSHIPS, RACES, SEXES, NATIVE_COUNTRIES

def generate_entry():
    random_entry = {}
    random_entry["age"] = max(round(np.random.normal(38.581647, 13.640433	)), 17)
    random_entry["workclass"] = random.choice(WORKCLASSES)
    random_entry["fnlgt"] = max(round(np.random.normal(1.897784e+05, 1.055500e+05)), 0)
    random_entry["education"] = random.choice(EDUCATIONS)
    random_entry["education-num"] = max(round(np.random.normal(10.080679, 2.572720)), 1)
    random_entry["marital-status"] = random.choice(MARITAL_STATUSES)
    random_entry["occupation"] = random.choice(OCCUPATIONS)
    random_entry["relationship"] = random.choice(RELATIONSHIPS)
    random_entry["race"] = random.choice(RACES)
    random_entry["sex"] = random.choice(SEXES)
    random_entry["capital-gain"] = max(round(np.random.normal(1077.648844, 7385.292085)),0)
    random_entry["capital-loss"] = max(round(np.random.normal(87.303830, 402.960219)),0)
    random_entry["hours-per-week"] = max(round(np.random.normal(40.437456, 12.347429)),1)
    random_entry["native-country"] = random.choice(NATIVE_COUNTRIES)
    return random_entry

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

#def generate_entry():


@pytest.fixture
def census_entries():
    return [first_census_entry, second_census_entry]


@pytest.fixture
def wrong_census_entries():
    return [empty_entry, missing_fields_entry, wrong_category_entry]

@pytest.fixture
def generate_entries():
    return [generate_entry() for i in range(5)]
