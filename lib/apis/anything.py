#
# All requests
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

router = APIRouter()


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


@router.get("/anything", summary = "Returns anything that is passed into the request.")
async def get(request: Request):
    retval = core(request)
    return(retval)


@router.post("/anything", summary = "Returns anything that is passed into the request.")
async def post(request: Request):
    data = await request.json()
    retval = core(request)
    retval["data"] = data
    return(retval)


@router.put("/anything", summary = "Returns anything that is passed into the request.")
async def put(request: Request):
    data = await request.json()
    retval = core(request)
    retval["data"] = data
    return(retval)


@router.patch("/anything", summary = "Returns anything that is passed into the request.")
async def patch(request: Request):
    data = await request.json()
    retval = core(request)
    retval["data"] = data
    return(retval)


@router.delete("/anything", summary = "Returns anything that is passed into the request.")
async def delete(request: Request):
    retval = core(request)
    return(retval)



