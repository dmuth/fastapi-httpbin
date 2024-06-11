#
# All requests
#

from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, Header, Request

from . import PrettyJSONResponse

router = APIRouter()


@router.get("/headers", summary = "Return the headers sent in the request.",
    response_class=PrettyJSONResponse)
async def get(request: Request):
    retval = {}
    retval = request.headers
    return(retval)


#
# Get our IP address
#
def get_ip(headers, client):

    if "fly-client-ip" in headers:
        retval = headers["fly-client-ip"]

    elif "x-forwarded-for" in headers:
        retval = headers["x-forwarded-for"]

    else:
        retval = client.host

    return(retval)


@router.get("/ip", summary = "Return the user's IP address.", 
    response_class=PrettyJSONResponse)
async def ip(request: Request):

    retval = {}

    ip = get_ip(request.headers, request.client)
    retval["ip"] = ip

    retval["message"] = []
    retval["message"].append("If you're looking for v4 or v6 specific endpoints, try /ip/v4 or /ip/v6.")
    retval["message"].append("If you want to ping this IP and graph the results, I built an app for that too: https://github.com/dmuth/grafana-network-monitor")

    return(retval)


@router.get("/ip/v4", summary = "Return the user's IPv4 address (if present).", 
    responses={
        200: {
            "description": "Return the user's IPv4 address, if present.",
        },
        422: {
            "description": "Returned if user came in over IPv6",
        },
    },
    response_class=PrettyJSONResponse)
async def ipv4(request: Request):

    retval = {}
    retval["ip"] = ""

    ip = get_ip(request.headers, request.client)

    if ":" not in ip:
        retval["ip"] = ip
    else:
        retval["message"] = "This does not appear to be a request made over IPv4"
        raise HTTPException(status_code = 422, detail = retval)

    return(retval)


@router.get("/ip/v6", summary = "Return the user's IPv6 address (if present).", 
    responses={
        200: {
            "description": "Return the user's IPv6 address, if present.",
        },
        422: {
            "description": "Returned if user came in over IPv4",
        },
    },
    response_class=PrettyJSONResponse)
async def ipv6(request: Request):

    retval = {}
    retval["ip"] = ""

    ip = get_ip(request.headers, request.client)

    if ":" in ip:
        retval["ip"] = ip
    else:
        retval["message"] = "This does not appear to be a request made over IPv6"
        raise HTTPException(status_code = 422, detail = retval)

    return(retval)



@router.get("/user-agent", summary = "Request the User Agent.",
    response_class=PrettyJSONResponse)
async def user_agent(request: Request):
    retval = {}
    retval["user-agent"] = request.headers["user-agent"]
    return(retval)


