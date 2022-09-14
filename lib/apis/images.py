#
# Redirect endpoints.
#

import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import FileResponse

from . import PrettyJSONResponse

router = APIRouter()


@router.get("/images/jpeg", summary = "Returns a JPEG image.",
    response_class = FileResponse,
    responses={
        200: {
            "content": {"image/jpeg": {}},
            "description": "Return an image in JPG format.",
        }
    }
    )
async def get(response: Response):
    return FileResponse("private/cheetah.jpeg")


@router.get("/images/png", summary = "Returns a PNG image.",
    response_class = FileResponse,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return an image in PNG format.",
        }
    }
    )
async def get(response: Response):
    return FileResponse("private/cheetah.png")


@router.get("/images/heic", 
    summary = "Returns a HEIC image. (This may not be displayed correctly in some browsers)",
    response_class = FileResponse,
    responses={
        200: {
            "content": {"image/heic": {}},
            "description": "Return an image in HEIC format.",
        }
    }
    )
async def get(response: Response):
    return FileResponse("private/cheetah.heic")


@router.get("/images/webp", summary = "Returns a Webp image.",
    response_class = FileResponse,
    responses={
        200: {
            "content": {"image/webp": {}},
            "description": "Return an image in Webp format.",
        }
    }
    )
async def get(response: Response):
    return FileResponse("private/cheetah.webp", headers = { "content-type": "image/webp"})



