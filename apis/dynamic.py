#
# Dynamic data.
#

import json
from uuid import uuid4
from time import sleep

from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, Header, Request, Query, Path
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.get("/uuid", summary = "Return a type 4 UUID.")
async def uuid(request: Request):
    retval = {}
    retval["uuid"] = uuid4()
    retval["message"] = "Do NOT use this endpoint as a source of randomness.  Please consider random.org instead."
    return(retval)


@router.get("/delay/{seconds}", summary = "Return a delayed response (max of 10 seconds).")
async def delay(request: Request, debug: bool | None = None, seconds: int = Path(example = 3)):

    if seconds < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {seconds} is < 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif seconds > 10:
        retval = {"type": "value_error.int.max_size", "message": f"Value {seconds} is > 10"}
        raise HTTPException(status_code = 422, detail = retval)

    if not debug:
        sleep(seconds)
    retval = {}
    retval["message"] = f"Slept for {seconds} seconds before returning!"
    if debug:
        retval["debug"] = "(Debug mode was on, so no actual sleeping happened.)"

    return(retval)


#
# Our coroutine to return results in a stream.
#
async def streamer(n):
    for i in range(n):
        row = {"response_number": (i + 1), "uuid": str(uuid4())}
        yield(json.dumps(row) + "\n")


@router.get("/stream/{n}", summary = "Steam n JSON responses.  (max of 100)")
async def delay(request: Request, n: int = Path(example = 3)):

    if n <= 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {n} is <= 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif n > 100:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} is > 100"}
        raise HTTPException(status_code = 422, detail = retval)

    return(StreamingResponse(streamer(n)))


