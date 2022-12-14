from pydantic import BaseModel, ValidationError, validator, Field

from enum import Enum

# age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary
# 39,State-gov,77516,Bachelors,13,Never-married,Adm-clerical,Not-in-family,White,Male,2174,0,40,United-States,<=50K

AGE_RANGE = (17, 90)
FNLGT_RANGE = (0, 1500000)
EDUCATION_NUM_RANGE = (1, 16)
CAPITAL_GAIN = (0, 100000)
CAPITAL_LOSS = (0, 4356)
HOURS_PER_WEEK = (1, 99)

WORKCLASSES = ["State-gov", "Self-emp-not-inc", "Private", "Federal-gov", "Local-gov", "?",
 "Self-emp-inc" ,"Without-pay", "Never-worked"]
EDUCATIONS = ["Bachelors", "HS-grad", "11th", "Masters", "9th", "Some-college", "Assoc-acdm",
 "Assoc-voc", "7th-8th", "Doctorate", "Prof-school", "5th-6th", "10th",
 "1st-4th", "Preschool", "12th"]
MARITAL_STATUSES = ["Never-married", "Married-civ-spouse", "Divorced", "Married-spouse-absent",
 "Separated", "Married-AF-spouse", "Widowed"]
OCCUPATIONS = ["Adm-clerical", "Exec-managerial", "Handlers-cleaners", "Prof-specialty", "Other-service",
               "Sales", "Craft-repair", "Transport-moving", "Farming-fishing", "Machine-op-inspct", "Tech-support",
               "?", "Protective-serv", "Armed-Forces", "Priv-house-serv"]
RELATIONSHIPS = ["Not-in-family", "Husband", "Wife", "Own-child", "Unmarried", "Other-relative"]
RACES = ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"]
SEXES = ["Male", "Female"]
NATIVE_COUNTRIES = ["United-States", "Cuba", "Jamaica", "India", "?", "Mexico", "South",
 "Puerto-Rico", "Honduras", "England", "Canada", "Germany", "Iran",
 "Philippines", "Italy", "Poland", "Columbia", "Cambodia", "Thailand", "Ecuador",
 "Laos", "Taiwan", "Haiti", "Portugal", "Dominican-Republic", "El-Salvador",
 "France", "Guatemala", "China", "Japan", "Yugoslavia", "Peru",
 "Outlying-US(Guam-USVI-etc)", "Scotland", "Trinadad&Tobago", "Greece",
 "Nicaragua", "Vietnam", "Hong", "Ireland", "Hungary", "Holand-Netherlands"]

SAMPLE_ENTRY = {
    "age": AGE_RANGE,
    "workclass": WORKCLASSES,
    "fnlgt": FNLGT_RANGE,
    "education": EDUCATIONS,
    "education-num": EDUCATION_NUM_RANGE,
    "marital-status": MARITAL_STATUSES,
    "occupation": OCCUPATIONS,
    "relationship": RELATIONSHIPS,
    "race": RACES,
    "sex": SEXES,
    "capital-gain": CAPITAL_GAIN,
    "capital-loss": CAPITAL_LOSS,
    "hours-per-week": HOURS_PER_WEEK,
    "native-country": NATIVE_COUNTRIES
}

first_census_entry = {
    "age": 20,
    "workclass": "State-gov",
    "fnlgt": 3000,
    "education": "Doctorate",
    "education-num": 10,
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


def all_lower(lst):
    return [x.lower() for x in lst]

class CensusEntry(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(alias='education-num')
    marital_status: str = Field(alias='marital-status')
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias='capital-gain')
    capital_loss: int = Field(alias='capital-loss')
    hours_per_week: int = Field(alias='hours-per-week')
    native_country: str = Field(alias='native-country')

    @validator('workclass')
    def validate_workclass(cls, workclass):
        if workclass.lower() not in all_lower(WORKCLASSES):
            raise ValueError(f'workclass {workclass} not valid, must be in {WORKCLASSES}')
        return workclass

    @validator('education')
    def validate_education(cls, education):
        if education.lower() not in all_lower(EDUCATIONS):
            raise ValueError(f'education {education} not valid, must be in {EDUCATIONS}')
        return education

    @validator('age')
    def validate_age(cls, age):
        if not AGE_RANGE[0] <= age <= AGE_RANGE[1]:
            raise ValueError(f'age {age} not valid, must be between {AGE_RANGE[0]} and {AGE_RANGE[1]}')
        return age

    @validator('education_num')
    def validate_education_num(cls, education_num):
        if not EDUCATION_NUM_RANGE[0] <= education_num <= EDUCATION_NUM_RANGE[1]:
            raise ValueError(f'education_num {education_num} not valid, must be between {EDUCATION_NUM_RANGE[0]} and {EDUCATION_NUM_RANGE[1]}')
        return education_num

    @validator('capital_gain')
    def validate_capital_gain(cls, capital_gain):
        if not CAPITAL_GAIN[0] <= capital_gain <= CAPITAL_GAIN[1]:
            raise ValueError(f'capital_gain {capital_gain} not valid, must be between {CAPITAL_GAIN[0]} and {CAPITAL_GAIN[1]}')
        return capital_gain

    @validator('capital_loss')
    def validate_capital_loss(cls, capital_loss):
        if not CAPITAL_LOSS[0] <= capital_loss <= CAPITAL_LOSS[1]:
            raise ValueError(
                f'capital_loss {capital_loss} not valid, must be between {CAPITAL_LOSS[0]} and {CAPITAL_LOSS[1]}')
        return capital_loss

    @validator('hours_per_week')
    def validate_hours_per_week(cls, hours_per_week):
        if not HOURS_PER_WEEK[0] <= hours_per_week <= HOURS_PER_WEEK[1]:
            raise ValueError(
                f'capital_loss {hours_per_week} not valid, must be between {HOURS_PER_WEEK[0]} and {HOURS_PER_WEEK[1]}')
        return hours_per_week

    @validator('marital_status')
    def validate_marital_status(cls, marital_status):
        if marital_status.lower() not in all_lower(MARITAL_STATUSES):
            raise ValueError(f'marital_status {marital_status} not valid, must be in {MARITAL_STATUSES}')
        return marital_status

    @validator('occupation')
    def validate_occupation(cls, occupation):
        if occupation.lower() not in all_lower(OCCUPATIONS):
            raise ValueError(f'occupation {occupation} not valid, must be in {OCCUPATIONS}')
        return occupation


    @validator('relationship')
    def validate_relationship(cls, relationship):
        if relationship.lower() not in all_lower(RELATIONSHIPS):
            raise ValueError(f'relationship {relationship} not valid, must be in {RELATIONSHIPS}')
        return relationship

    @validator('race')
    def validate_race(cls, race):
        if race.lower() not in all_lower(RACES):
            raise ValueError(f'race {race} not valid, must be in {RACES}')
        return race

    @validator('sex')
    def validate_sex(cls, sex):
        if sex.lower() not in all_lower(SEXES):
            raise ValueError(f'sex {sex} not valid, must be in {SEXES}')
        return sex

    @validator('native_country')
    def validate_native_country(cls, native_country):
        if native_country.lower() not in all_lower(NATIVE_COUNTRIES):
            raise ValueError(f'native_country {native_country} not valid, must be in {NATIVE_COUNTRIES}')
        return native_country

