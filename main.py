# Put the code for your API here.
# bar.py

from fastapi import FastAPI
from pydantic import BaseModel
from values.census_entry import CensusEntry
from ml.data import process_data
from ml.model import inference
import pandas as pd
import joblib
import os
from fastapi.encoders import jsonable_encoder
import numpy as np

dirname = os.path.join(os.getcwd(), 'model', 'v1')
# Add code to load in the data.
model = joblib.load(os.path.join(dirname, 'model'))
encoder = joblib.load(os.path.join(dirname, 'encoder'))
lb = joblib.load(os.path.join(dirname, 'lb'))
cat_features = joblib.load(os.path.join(dirname, 'cat_features'))
# API Deployment


app = FastAPI()


@app.post("/print_out")
async def print_out(body: CensusEntry):
    return body


