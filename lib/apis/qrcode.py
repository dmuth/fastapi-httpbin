#
# QR Code endpoints
#

from io import BytesIO
import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import FileResponse

import qrcode

router = APIRouter()


@router.post("/qrcode", summary = "Returns a QR code in PNG format.",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return a QR Code in PNG format.",
        }
    },
    response_class=Response,
    )
async def qrcode_post(url: str = "https://www.youtube.com/watch?v=nCEemcXzERk",
    box_size: int = 10, border: int = 2):

    #
    # Generate our QR Code
    #
    qr = qrcode.QRCode(version = 1, box_size = box_size, border = border)
    qr.add_data(url)
    qr.make()
    img = qr.make_image(fill_color = 'black', back_color = 'white')

    #
    # And put it into a buffer that we'll return
    #
    bytes = BytesIO()
    img.save(bytes, format = "png")
    retval = bytes.getvalue()

    return Response(content = retval, media_type="image/png")


@router.post("/qr", include_in_schema = False)
async def qr_post():
    return RedirectResponse(f"/qrcode", status_code = 302)


@router.post("/qr-code", include_in_schema = False)
async def qr_code_post():
    return RedirectResponse(f"/qrcode", status_code = 302)



