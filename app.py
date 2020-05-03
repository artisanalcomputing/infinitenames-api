import json
import random

from fastapi import FastAPI
import collections

def get_random_names(num):
    # read file
    with open('names.json', 'r') as myfile:
        data=myfile.read()
    # parse file
    names = json.loads(data)
    if not num:
        return [random.choice(names)]
    else:
        randomItems = [];
        for i in range(num):
            randomItems.append(random.choice(names))
        return randomItems;

app = FastAPI()

@app.get("/")
async def root():
    return ("Welcome to infinitejest-names")

@app.get("/get-name")
async def get_names(num: int = None):
    random_names = get_random_names(num)
    return {'random_names': random_names}
