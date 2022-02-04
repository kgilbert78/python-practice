from typing import Optional
from fastapi import FastAPI
from typing import List # I added for testing

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

database: List[dict] = [] # I added for testing

server = FastAPI()

@server.get("/")
async def root():
    return {"message": "Hello World!"}

@server.get("/items/") # I added for testing
async def send_database():
    return database

@server.post("/items/")
async def create_item(item: Item): # capital Item is type declaration
    # print(item) # print to backend terminal
    # return item # doesn't clear optional values from prior requests if new values aren't included in next request.
    # return {item.name, item.description, item.price, item.tax} # this does clear them. put request probably better though.

    # print(type(item)) # <class 'main.Item'>

    item_dict = item.dict() # python method to convert to dict: https://www.w3schools.com/python/ref_func_dict.asp (see also comment 2 lines above)
    if item.tax:
        # can access all the attributes of the model object directly
        add_tax = item.price + item.tax
        price_with_tax = round(add_tax, 2)
        # python method to modify contents of dict: https://www.w3schools.com/python/ref_dictionary_update.asp
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# REQUEST BODY & ROUTE PARAMETERS AT THE SAME TIME (recognizes params that match route params should be taken from the path and those declared to be Pydantic models should be taken from the request body (item: Item) )
@server.put("/items/{item_id}")
async def create_item_2params(item_id: int, item: Item):
    database.append({"item_id": item_id, **item.dict()}) # I added for testing
    return {"item_id": item_id, **item.dict()}
    # ** explained: "A double asterisk ** denotes dictionary unpacking. Its operand must be a mapping. Each mapping item is added to the new dictionary." from https://docs.python.org/3/reference/expressions.html#dictionary-displays, mapping info: https://docs.python.org/3/glossary.html#term-mapping
    
    # response in Postman:
    # {
    #     "item_id": 2,
    #     "name": "Foo2",
    #     "description": "testing how ** unpacking of item.dict() works",
    #     "price": 15.99,
    #     "tax": 0.8
    # }
    # print(item) above the return statement prints non-dictionary without item_id added:
    # name='Foo2' description='testing how ** unpacking of item.dict() works' price=15.99 tax=0.8

# REQUEST BODY & ROUTE & QUERY PARAMETERS AT THE SAME TIME
@server.put("/items/{item_id}")
async def create_item_3params(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    database.append(result) # I added for testing
    return result

# also skip ahead to here https://fastapi.tiangolo.com/tutorial/body-updates/ so I can build ip-address-3 with put endpoint? might also need to do https://fastapi.tiangolo.com/tutorial/encoder/ first. and cors: https://fastapi.tiangolo.com/tutorial/cors/ ...then go back to stuff in between.


@server.get("/items-type-conv/{item_id}")
async def read_item_conv(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
        # python method to modify contents of dict: https://www.w3schools.com/python/ref_dictionary_update.asp
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

    # Postman: http://localhost:8000/items/3?q=testing
    # {
    #     "item_id": 3,
    #     "name": "FooBar",
    #     "description": null,
    #     "price": 25.0,
    #     "tax": 1.25
    # }