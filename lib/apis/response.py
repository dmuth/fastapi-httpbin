#
# All responses.
#

import re

from fastapi import APIRouter, Query, Body, Path
from fastapi import FastAPI, Header, Request, Response, HTTPException

from . import PrettyJSONResponse

router = APIRouter()


@router.get("/cache", 
    summary = "Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.")
async def cache(request: Request, response: Response):
    if "if-modified-since" in request.headers:
        response.status_code = 304
    elif "if-none-match" in request.headers:
        response.status_code = 304

    return(None)


@router.get("/cache/{seconds}", summary = "Sets a Cache-Control header for n seconds.")
async def cache_seconds(request: Request, response: Response, seconds: int = Path(example = 3)):
    response.headers["cache-control"] = f"public, max-age={seconds}"


@router.get("/etag/{etag}", 
    summary = "Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.")
async def etag(request: Request, response: Response, etag: str = Path(example = "test-etag")):
    response.headers["etag"] = etag

    if "if-none-match" in request.headers:
        if request.headers["if-none-match"] == etag:
            response.status_code = 304

    elif "if-match" in request.headers:
        if request.headers["if-match"] != etag:
            response.status_code = 412



@router.get("/response-headers",
    summary = "Set arbitrary headers in the response.  Input strings should be in the format of 'header:value'.",
    response_class=PrettyJSONResponse)
def response_headers_get(response: Response, headers: list[str] = Query(default = [])):

    #
    # Sanity check our headers, since we can't use the regex parameter on a list.
    #
    for header in headers:
        if not re.search("^[^:]+:[^:]+$", header):
            retval = {"type": "value_error.str.format",
                "message": f"Parameter '{header}' not in format 'header:value"}
            raise HTTPException(status_code = 422, detail = retval)

    retval = {"message": f"{len(headers)} headers set in response"}
        
    for header in headers:
        key, value = header.split(":")
        response.headers[key] = value
    return(retval)



