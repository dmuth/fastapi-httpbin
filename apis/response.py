#
# All responses.
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request, Response

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
async def cache_seconds(request: Request, response: Response, seconds: int):
    response.headers["cache-control"] = f"public, max-age={seconds}"


@router.get("/etag/{etag}", 
    summary = "Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.")
async def etag(request: Request, response: Response, etag: str):
    response.headers["etag"] = etag

    if "if-none-match" in request.headers:
        if request.headers["if-none-match"] == etag:
            response.status_code = 304

    elif "if-match" in request.headers:
        if request.headers["if-match"] != etag:
            response.status_code = 412


