from typing import Optional
from fastapi import FastAPI

# need pydantic's BaseModel class to declare a request body
from pydantic import BaseModel

# declare data model as a class that inherits from BaseModel
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # when a model attribute has a default value it is not required. otherwise it is required. None makes it just optional.
    # both valid (try in Postman): 
        # {"name": "Foo", "description": "An optional description", "price": 45.2, "tax": 3.5} 
        # {"name": "Foo", "price": 45.2}

server = FastAPI()

@server.get("/")
async def root():
    return {"message": "Hello World!"}

@server.post("/items/")
async def create_item(item: Item): # capital Item is type declaration
    # print(item) # print to backend terminal
    return item # doesn't clear optional values from prior requests if new values aren't included in next request.
    # return {item.name, item.description, item.price, item.tax} # does clear them. put request probably better though.



# ... left off here: https://fastapi.tiangolo.com/tutorial/body/#results

# also skip ahead to here https://fastapi.tiangolo.com/tutorial/body-updates/ so I can build ip-address-3 with put endpoint? might also need to do https://fastapi.tiangolo.com/tutorial/encoder/ first. then go back to stuff in between.