
from typing import Union

from fastapi import FastAPI, Header, Request
from pydantic import BaseModel


app = FastAPI()


#
# TODO:
#
# X HTTP Methods
# - Push to GitHub private repo
# 2 Status Codes
# 3 Figure out how to group endpoints in docs (tags?)
# 4 Make main page go to docs
# - Write some unit tests
# - Deploy to Deta
# - Next batch of docs

@app.get("/get")
async def get(request: Request):

	retval = {}

	retval["args"] = request.query_params
	retval["headers"] = request.headers
	retval["source"] = {
		"ip": request.client[0],
		"port": request.client[1]
		}
	retval["url"] = request.url

	return(retval)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
#def read_root():
async def read_root():
	return {"Hello": "World"}


@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
async def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


