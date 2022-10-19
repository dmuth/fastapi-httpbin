#
# QR Code endpoints
#

from io import BytesIO
import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import qrcode

router = APIRouter()


@router.post("/form/post", summary = "Process a sample login",
    responses={
        200: {
            "description": "Valid credentials were supplied. (username: dmuth, password: password)",
        },
        401: {
            "description": "Invalid credentials were supplied"
        }
    },
    response_class=Response
    )
async def qrcode_post_form(username: str = Form(),
    password: str = Form()):

    retval = {}

    retval["status"] = "success"
    retval["errors"] = []

    if username != "dmuth":
        retval["status"] = "error"
        retval["errors"].append("Username did not match, expected 'dmuth'")

    if password != "password":
        retval["status"] = "error"
        retval["errors"].append("Password did not match, expected 'password'")

    if retval["status"] == "success":
        return JSONResponse(retval, media_type = "text/plain")

    raise HTTPException(status_code = 401, detail = retval)


