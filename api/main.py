# Put the code for your API here.
# bar.py
from fastapi import FastAPI, HTTPException
from values.census_entry import CensusEntry, SAMPLE_ENTRY
from ml.model import inference
import pandas as pd
import joblib
import os
import numpy as np
import uvicorn
import pprint

from pydantic import BaseSettings, ValidationError


class Settings(BaseSettings):
    dirname: str = "model/latest"

settings = Settings()
dirname = settings.dirname

# Add code to load in the data.
model = joblib.load(os.path.join(dirname, 'model'))
encoder = joblib.load(os.path.join(dirname, 'encoder'))
lb = joblib.load(os.path.join(dirname, 'lb'))
cat_features = joblib.load(os.path.join(dirname, 'cat_features'))
# API Deployment


description= f"""
This API allows you texecute a prediction based on provided features of a family, to guess whether the family is expected to make more or less than 50k. 

## Input Data

A census_entry contains following fields, with the accepted ranges and values

```
{pprint.pformat(SAMPLE_ENTRY, compact=True, sort_dicts=False)}
```

## Method

You can execute a prediction with the *predict* method:
"""


app = FastAPI(
    title="Income Prediction",
    description=description
)


@app.post("/print_out")
async def print_out(body: CensusEntry):
    try:
        return body
    except Exception as e:
        print(e)
        raise HTTPException(status_code=422, detail=e)

@app.get("/")
async def welcome():
    result = "Welcome to CENSUS API. " \
             " You have to execute a post call to /predict passing a valid census entry in the body. " \
             " A valid census_entry is a json file containing following fields: " \
             " age, workclass, fnlgt, education, education-num, marital-status, occupation " \
             " relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country"
    return {"result": result}

@app.post("/predict")
async def predict(census_entry: CensusEntry):
    try:
        census_dict = census_entry.dict(by_alias=True)
        census_dict_frame = ({k: [v] for k, v in census_dict.items()})
        data = pd.DataFrame.from_dict(census_dict_frame)

        X_categorical = data[cat_features].values
        X_continuous = data.drop(*[cat_features], axis=1).values

        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate([X_continuous, X_categorical], axis=1)
        preds = inference(model, X)
        return {"result": ">50K" if preds[0] else "<=50k"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=422, detail=e)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info")