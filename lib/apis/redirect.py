#
# Redirect endpoints.
#

import random

from fastapi import APIRouter, FastAPI, Header, Response, Path, HTTPException, Depends
from fastapi.responses import RedirectResponse, JSONResponse

from . import PrettyJSONResponse
from . import RedirectQueryParams

router = APIRouter()


def core(response, n, code):

    #
    # Do some sanity checking.
    # I originally wanted a custom exception, but it got *really* challenging figuring
    # out how to add an exception while in a router, and adding it to app didn't help either. :-(
    #
    if n > 20:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} is > 20"}
        raise HTTPException(status_code = 422, detail = retval)

    if n > 1:
        return RedirectResponse(f"/redirect/{n - 1}?code={code}", status_code = code)

    if n <= 1:
        return RedirectResponse(f"/redirect/final?code={code}", status_code = code)

    return(retval)


@router.get("/redirect/{n}", 
    summary = "302 Redirects n times. (Note that Swagger follows redirects, so use the Curl command to see redirect headers.",
    response_class=PrettyJSONResponse)
async def get(response: Response, 
    n: int = Path(example = 3, description = "Number of redirects to perform"),
    params: RedirectQueryParams = Depends()
    ):
    response = core(response, n, params.code)
    response.headers["x-http-redirect-code"] = str(params.code)
    return(response)


@router.post("/redirect/{n}", 
    summary = "302 Redirects n times. (Note that Swagger follows redirects, so use the Curl command to see redirect headers.",
    response_class=PrettyJSONResponse)
async def post(response: Response, 
    n: int = Path(example = 3, description = "Number of redirects to perform"),
    params: RedirectQueryParams = Depends()
    ):
    response = core(response, n, params.code)
    response.headers["x-http-redirect-code"] = str(params.code)
    return(response)


@router.put("/redirect/{n}", 
    summary = "302 Redirects n times. (Note that Swagger follows redirects, so use the Curl command to see redirect headers.",
    response_class=PrettyJSONResponse)
async def put(response: Response, 
    n: int = Path(example = 3, description = "Number of redirects to perform"),
    params: RedirectQueryParams = Depends()
    ):
    response = core(response, n, params.code)
    response.headers["x-http-redirect-code"] = str(params.code)
    return(response)


@router.patch("/redirect/{n}", 
    summary = "302 Redirects n times. (Note that Swagger follows redirects, so use the Curl command to see redirect headers.",
    response_class=PrettyJSONResponse)
async def patch(response: Response, 
    n: int = Path(example = 3, description = "Number of redirects to perform"),
    params: RedirectQueryParams = Depends()
    ):
    response = core(response, n, params.code)
    response.headers["x-http-redirect-code"] = str(params.code)
    return(response)


@router.delete("/redirect/{n}", 
    summary = "302 Redirects n times. (Note that Swagger follows redirects, so use the Curl command to see redirect headers.",
    response_class=PrettyJSONResponse)
async def delete(response: Response, 
    n: int = Path(example = 3, description = "Number of redirects to perform"),
    params: RedirectQueryParams = Depends()
    ):
    response = core(response, n, params.code)
    response.headers["x-http-redirect-code"] = str(params.code)
    return(response)



