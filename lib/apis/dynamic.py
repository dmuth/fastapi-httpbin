#
# Dynamic data.
#

from io import BytesIO
import json
from uuid import uuid4, UUID
import asyncio
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, Header, Request, Query, Path, Response
from fastapi.responses import StreamingResponse

import qrcode

from . import PrettyJSONResponse

router = APIRouter()


#
# Worker function to generate our QR Code.
#
def get_qr_code(uuid):

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)
    qr.add_data(uuid)
    qr.make()
    img = qr.make_image(fill_color = 'black', back_color = 'white')

    #
    # And put it into a buffer that we'll return
    #
    bytes = BytesIO()
    img.save(bytes, format = "png")
    retval = bytes.getvalue()

    return(retval)


@router.get("/uuid", summary = "Return a type 4 UUID.",
    response_class=PrettyJSONResponse)
async def uuid(request: Request):

    url = request.url._url
    uuid = uuid4()

    retval = {}
    retval["uuid"] = uuid
    retval["messages"] = [
        "Do NOT use this endpoint as a source of randomness.  Please consider random.org instead.",
        f"If you'd like a random QR code instead, try {url}/qrcode",
        f"If you'd like *this* UUID as a QR code, try {url}/qrcode/{uuid}",
        ]
    retval["timestamp"] = datetime.now(timezone.utc).isoformat()
    return(retval)


@router.get("/uuid/qrcode", summary = "Return a QR code of a type 4 UUID.",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return a QR Code in PNG format.",
        }
    },
    response_class=Response)
async def uuid_qrcode():
    uuid = uuid4()
    qrcode = get_qr_code(uuid)
    return Response(content = qrcode, media_type="image/png")


@router.get("/uuid/qrcode/{uuid}", summary = "Return a QR code of a *specified* type 4 UUID.",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return a QR Code in PNG format.",
        }
    },
    response_class=Response)
async def uuid_qrcode_qrcode(uuid: str):

    try:
        UUID(uuid)

    except ValueError as e:
        retval = {"type": "value_error.str.validation", 
            "message": f"Value '{uuid}' must be a type 4 UUID in the format of 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx' where x is any hexidecimal digit and y is in the set (8, 9, a, b)"}
        raise HTTPException(status_code = 422, detail = retval)

    qrcode = get_qr_code(uuid)
    return Response(content = qrcode, media_type="image/png")


@router.get("/delay/{seconds}", summary = "Return a delayed response (max of 10 seconds).",
    response_class=PrettyJSONResponse)
async def delay(request: Request, 
    debug: bool | None = None, 
    seconds: int = Path(example = 3)):

    retval = {}
    retval["timestamps"] = {}
    retval["timestamps"]["start"] = datetime.now(timezone.utc).isoformat()
    

    if seconds < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {seconds} is < 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif seconds > 10:
        retval = {"type": "value_error.int.max_size", "message": f"Value {seconds} is > 10"}
        raise HTTPException(status_code = 422, detail = retval)


    if not debug:
        await asyncio.sleep(seconds)

    retval["message"] = f"Slept for {seconds} seconds before returning!"
    retval["timestamps"]["end"] = datetime.now(timezone.utc).isoformat()

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
async def stream(request: Request, n: int = Path(example = 3)):

    if n <= 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {n} is <= 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif n > 100:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} is > 100"}
        raise HTTPException(status_code = 422, detail = retval)

    return(StreamingResponse(streamer(n)))


#
# Add a newline onto the end of the buffer.
#
def add_newline(buf):

    if buf:
        buf = list(buf)
        buf[len(buf) - 1] = "\n"
        buf = "".join(buf)

    return(buf)


#
# Return results in a stream with a second pause between them.
#
# @param int n Number of characters to sendin total
# @param int rate How many characters to send each second.
# @param bool debug If set, we won't sleep.
#
async def streamer_rate(n, rate, debug):

    buf = ""
    num_left = n
    while True:

        for i in (range(48, 123)):

            #
            # Add a character to our buffer, and when we hit the limit
            # change the last character to a newline and yield that buffer.
            #
            buf += chr(i)
            if len (buf) >= rate:
                buf = add_newline(buf)
                yield(buf)
                if not debug:
                    await asyncio.sleep(1)
                buf = ""

            #
            # If we're out of characters to display, return what we have then break out of this loop.
            #
            num_left -= 1
            if num_left <= 0:
                buf = add_newline(buf)
                yield(buf)
                break

        if num_left <= 0:
            break


@router.get("/stream/chars/{n}/{rate}", 
    summary = "Stream n bytes (max 100K) at a rate of rate per second. Max time is 20 seconds.")
async def stream_chars(request: Request, 
    debug: bool | None = None, 
    n: int = Path(example = 128), 
    rate: int = Path(example = 50)):

    percent = (rate / n) * 100

    if n < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {n} bytes is <= 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif n > 102400:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} bytes is > 102400"}
        raise HTTPException(status_code = 422, detail = retval)

    elif percent < 5:
        retval = {"type": "value_error.int.min_size", 
            "message": f"{n} / {rate} = {percent:.2f} percent.  This means runtime will take longer than 20 seconds.  Please try a larger rate."}
        raise HTTPException(status_code = 422, detail = retval)

    return(StreamingResponse(streamer_rate(n, rate, debug)))


#
# Return results in a stream with a second pause between them.
#
# @param int n Number of characters to sendin total
# @param int rate How many characters to send each second.
# @param bool debug If set, we won't sleep.
#
async def streamer_rate_complete(n, rate, debug):

    buf = ""
    num_left = n
    num_loops_left = 10
    done = False

    while True:

        for i in (range(48, 123)):

            #
            # Add a character to our buffer, and when we hit the limit
            # change the last character to a newline and yield that buffer.
            #
            buf += chr(i)
            if len (buf) >= rate:
                buf = add_newline(buf)
                yield(buf)
                if not debug:
                    await asyncio.sleep(1)
                buf = ""
                num_loops_left -= 1

            #
            # If we're out of characters to display, return what we have then break out of this loop.
            #
            num_left -= 1
            if num_left <= 0:
                if buf:
                    buf = add_newline(buf)
                    yield(buf)
                done = True
                break

            if num_loops_left <= 0:
                done = True
                break

        if done:
            break

    #
    # If we have any charcters left to display, dump them out all at once.
    #
    if num_left:

        buf = ""
        done = False

        while True:

            for i in (range(48, 123)):
                buf += chr(i)
                num_left -= 1

                if num_left <= 0:
                    if buf:
                        buf = add_newline(buf)
                        yield(buf)
                    done = True
                    break

            if done:
                break


@router.get("/stream/chars/complete/{n}/{rate}", 
    summary = "Stream n bytes (max 100K) at a rate of rate per second. Any outstanding characters due to a low rate will be sent at the very end.  Max time is 10 seconds.")
async def stream_chars_complete(request: Request, 
    debug: bool | None = None, 
    n: int = Path(example = 128), 
    rate: int = Path(example = 50)):

    percent = (rate / n) * 100

    if n < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value {n} bytes is <= 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif n > 102400:
        retval = {"type": "value_error.int.max_size", "message": f"Value {n} bytes is > 102400"}
        raise HTTPException(status_code = 422, detail = retval)

    elif rate <= 0:
        retval = {"type": "value_error.int.min_size", "message": f"Value rate {rate} is <= 0"}
        raise HTTPException(status_code = 422, detail = retval)

    return(StreamingResponse(streamer_rate_complete(n, rate, debug)))



