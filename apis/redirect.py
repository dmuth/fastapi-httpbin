#
# Redirect endpoints.
#

import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse


router = APIRouter()


def core(response, n):

    #
    # Do some sanity checking.
    # I originally wanted a custom exception, but it got *really* challenging figuring
    # out how to add an exception while in a router, and adding it to app didn't help either. :-(
    #
    if n > 20:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} is > 20"}
        raise HTTPException(status_code = 422, detail = retval)

    if n > 1:
        return RedirectResponse(f"/redirect/{n - 1}", status_code = 302)

    return RedirectResponse(f"/get", status_code = 302)


@router.get("/redirect/{n}", summary = "302 Redirects n times")
async def get(response: Response, 
    n: int
    ):
    response = core(response, n)
    return(response)


@router.post("/redirect/{n}", summary = "302 Redirects n times")
async def post(response: Response, 
    n: int
    ):
    response = core(response, n)
    return(response)


@router.put("/redirect/{n}", summary = "302 Redirects n times")
async def put(response: Response, 
    n: int
    ):
    response = core(response, n)
    return(response)


@router.patch("/redirect/{n}", summary = "302 Redirects n times")
async def patch(response: Response, 
    n: int
    ):
    response = core(response, n)
    return(response)


@router.delete("/redirect/{n}", summary = "302 Redirects n times")
async def delete(response: Response, 
    n: int
    ):
    response = core(response, n)
    return(response)



