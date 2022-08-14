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


@router.get("/headers", summary = "Return the headers sent in the request.")
async def get(request: Request):
    retval = {}
    retval = request.headers
    return(retval)


@router.get("/ip", summary = "Return the user's IP address.")
async def ip(request: Request):
    retval = {}
    retval["ip"] = request.client[0]
    return(retval)


@router.get("/user-agent", summary = "Request the User Agent.")
async def user_agent(request: Request):
    retval = {}
    retval["user-agent"] = request.headers["user-agent"]
    return(retval)


