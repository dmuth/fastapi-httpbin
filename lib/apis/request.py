#
# All requests
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

from . import PrettyJSONResponse

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


@router.get("/headers", summary = "Return the headers sent in the request.",
    response_class=PrettyJSONResponse)
async def get(request: Request):
    retval = {}
    retval = request.headers
    return(retval)


@router.get("/ip", summary = "Return the user's IP address.", 
    response_class=PrettyJSONResponse)
async def ip(request: Request):
    retval = {}

    if "fly-client-ip" in request.headers:
        retval["ip"] = request.headers["fly-client-ip"]

    elif "x-forwarded-for" in request.headers:
        retval["ip"] = request.headers["x-forwarded-for"]

    else:
        retval["ip"] = request.client[0]

    return(retval)


@router.get("/user-agent", summary = "Request the User Agent.",
    response_class=PrettyJSONResponse)
async def user_agent(request: Request):
    retval = {}
    retval["user-agent"] = request.headers["user-agent"]
    return(retval)


