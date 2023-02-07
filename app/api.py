"""
Module for api requests
"""
# import re
from fastapi import FastAPI
from src import read
from src import transform


app = FastAPI()

data_hold = []


@app.post("/load")
async def create_pipeline(file: str):
    """function to get user data"""
    data = read.create_data_object(file)
    data_hold.append(data)
    return {"message": "Data successfully uploaded"}


@app.get("/summary")
async def data_summary():
    """function to create data summary"""
    data = data_hold[0]
    load_summary = transform.create_data_report(data)
    return load_summary


@app.get("/extract/{task}")
async def choose_transformation(task: str):
    """function to choose transformation to apply to data"""
    data = data_hold[0]
    if task == "missing":
        clean = data.dropna()
    data_hold.append(clean)
    result = clean.to_json(orient="records")
    return result


@app.get("/extract")
async def extract():
    """function to to return formatted data as csv"""
    data = data_hold[1]
    cleandf = data.to_json(orient="records")
    return cleandf
