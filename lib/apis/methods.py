#
# All requests
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

from . import logger

router = APIRouter()

import json

#
# Our core function to return the same data for each request.
#
def core(request: Request):

    retval = {}

    retval["args"] = request.query_params
    retval["headers"] = request.headers
    retval["source"] = {
        "ip": request.client[0],
        "port": request.client[1]
        }
    retval["url"] = request.url

    return(retval)


@router.get("/get", summary = "The request's GET parameters.")
async def get(request: Request):
    retval = core(request)
    return(retval)


@router.post("/post", summary = "The request's POST parameters. (Use -d in curl to specify data in JSON format)")
async def post(request: Request):

    data = {}

    try:
        data = await request.json()
    except json.decoder.JSONDecodeError as e:
        logger.warn(f"{__name__}:post(): Caught error deserializing JSON: {e}")

    retval = core(request)
    retval["data"] = data
    return(retval)


@router.put("/put", summary = "The request's PUT parameters. (Use -d in curl to specify data in JSON format)")
async def put(request: Request):

    data = {}

    try:
        data = await request.json()
    except json.decoder.JSONDecodeError as e:
        logger.warn(f"{__name__}:put(): Caught error deserializing JSON: {e}")

    retval = core(request)
    retval["data"] = data
    return(retval)


@router.patch("/patch", summary = "The request's PATCH parameters. (Use -d in curl to specify data in JSON format)")
async def patch(request: Request):

    data = {}

    try:
        data = await request.json()
    except json.decoder.JSONDecodeError as e:
        logger.warn(f"{__name__}:patch(): Caught error deserializing JSON: {e}")

    retval = core(request)
    retval["data"] = data
    return(retval)


@router.delete("/delete", summary = "The request's DELETE parameters.")
async def delete(request: Request):
    retval = core(request)
    return(retval)



