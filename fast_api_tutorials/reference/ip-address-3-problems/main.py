# This is sending back the right thing in the put but not saving it. And it's only sending back the right thing when I return config_log[len(config_log) - 1] it sends the wrong thing when I return current_config. Also when you do get after put it goes back to the original. No need to save all configs in a list but I couldn't get it to work with reassigning the variable.

from typing import Dict, Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel

config_log = []
# saved_config = ""

# https://www.geeksforgeeks.org/read-json-file-using-python/
sample_config = open('./data/sampleConfig.json')
data = json.load(sample_config)
sample_config.close()
# saved_config = data
config_log.append(data)

current_config = config_log[len(config_log) - 1]

print("config log at top", config_log)

# print(config_log[len(config_log) - 1])
# config_log.append(hard_coded_update)
# print(config_log[len(config_log) - 1])

class Config(BaseModel):
    algo3: Dict[str, Union[int, str]]
    override: Dict[str, str]
    intraframe: Dict[str, int]
    sensor: Dict[str, int]
    flags: Dict[str, bool]
    # not sure if this will work - need to account for all possibilities of config keys and values

server = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
server.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@server.get("/")
async def root():
    return {"Hello": "FastAPI!"}

@server.get("/configjson/")
async def send_config():
    print("config log in get", config_log)
    # return current_config
    return config_log[len(config_log) - 1]

@server.put("/configjson/")
async def update_config(config_received: Config):
    config_to_add = config_received.dict()
    # config_to_update = json.dumps(config_received)
    # current_config = config_to_update

    config_log.append(config_to_add)

    print("config log in put", config_log)

    # print("in put req:", current_config)
    # return current_config

    current_config = config_log[len(config_log) - 1]

    algo3 = current_config.get("algo3")
    deviceConfigName = algo3.get("deviceConfigName")
    print("deviceConfigName from current_config in put:", deviceConfigName)
    algo3 = config_to_add.get("algo3")
    deviceConfigName = algo3.get("deviceConfigName")
    print("deviceConfigName from config_to_add in put:", deviceConfigName)

    return config_log[len(config_log) - 1]
    # return current_config