#
# Final endpoints for redirects, which will include the original status code.
# These are hidden from the Swagger documentation, because there's no real point
# in showing them to the user, and they'll just clutter up the site.
#

import random

from fastapi import APIRouter, FastAPI, Header, Response, Path, HTTPException, Depends
from fastapi.responses import RedirectResponse, JSONResponse

from . import PrettyJSONResponse
from . import RedirectQueryParams

router = APIRouter()


@router.get("/redirect/final",
    summary = "Final endpoint after one or more redirects.",
    response_class=PrettyJSONResponse,
    include_in_schema = False)
async def get(
    response: Response,
    params: RedirectQueryParams = Depends()
    ):
    response = {
        "message": "Reached the end of our redirects!",
        "code": params.code
        }
    return(response)

@router.put("/redirect/final",
    summary = "Final endpoint after one or more redirects.",
    response_class=PrettyJSONResponse,
    include_in_schema = False)
async def get(
    response: Response,
    params: RedirectQueryParams = Depends()
    ):
    response = {
        "message": "Reached the end of our redirects!",
        "code": params.code
        }
    return(response)

@router.post("/redirect/final",
    summary = "Final endpoint after one or more redirects.",
    response_class=PrettyJSONResponse,
    include_in_schema = False)
async def get(
    response: Response,
    params: RedirectQueryParams = Depends()
    ):
    response = {
        "message": "Reached the end of our redirects!",
        "code": params.code
        }
    return(response)

@router.delete("/redirect/final",
    summary = "Final endpoint after one or more redirects.",
    response_class=PrettyJSONResponse,
    include_in_schema = False)
async def get(
    response: Response,
    params: RedirectQueryParams = Depends()
    ):
    response = {
        "message": "Reached the end of our redirects!",
        "code": params.code
        }
    return(response)

@router.patch("/redirect/final",
    summary = "Final endpoint after one or more redirects.",
    response_class=PrettyJSONResponse,
    include_in_schema = False)
async def get(
    response: Response,
    params: RedirectQueryParams = Depends()
    ):
    response = {
        "message": "Reached the end of our redirects!",
        "code": params.code
        }
    return(response)


