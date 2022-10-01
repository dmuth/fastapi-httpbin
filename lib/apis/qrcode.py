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


#
# Worker function to generate our QR Code.
#
def get_qr_code(url, box_size, border):

    #
    # Do some sanity checks
    #
    if box_size < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Box_size {box_size} is < 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif border < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Border {border} is < 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif box_size > 20:
        retval = {"type": "value_error.int.max_size", "message": f"Box_size {box_size} is > 20"}
        raise HTTPException(status_code = 422, detail = retval)

    elif border > 20:
        retval = {"type": "value_error.int.max_size", "message": f"Border {border} is > 20"}
        raise HTTPException(status_code = 422, detail = retval)

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

    return(retval)


@router.post("/qrcode/form", summary = "Returns a QR Code in PNG format from form submission.",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return a QR Code in PNG format.",
        }
    },
    response_class=Response
    )
async def qrcode_post_form(url: str = Form(),
    box_size: int = Form(), border: int = Form()):
    qrcode = get_qr_code(url, box_size, border)
    return Response(content = qrcode, media_type="image/png")


#
# Create our QRCode model.
# This is necessary so that the JSON is passed into the body.  Otherwise FastAPI
# will want the JSON to be passed in as GET-method data, even for a POST.  If that
# sounds weird, it's because it is.  That is maybe the sole issue I have with FastAPI.
#
class QRCode(BaseModel):
    url: str = Field(default = "https://www.youtube.com/watch?v=nCEemcXzERk",
        min_length = 10, max_length = 1000)
    box_size: int = Field(default = 10, gt = 0, le = 20)
    border: int = Field(default = 2, gt = 0, le = 20)
    
@router.post("/qrcode/json", summary = "Returns a QR code in PNG format from POSTed JSON.",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return a QR Code in PNG format.",
        }
    },
    response_class=Response
    )
async def qrcode_post(data: QRCode):
    url = data.url
    box_size = data.box_size
    border = data.border
    #print("Debugging", url, box_size, border) # Debugging
    qrcode = get_qr_code(url, box_size, border)
    return Response(content = qrcode, media_type="image/png")


@router.get("/qrcode", include_in_schema = False)
async def qrcode_get():
    return RedirectResponse(f"/qrcode/", status_code = 302)


@router.post("/qr", include_in_schema = False)
async def qr_post():
    return RedirectResponse(f"/qrcode/", status_code = 302)


@router.post("/qr-code", include_in_schema = False)
async def qr_code_post():
    return RedirectResponse(f"/qrcode/", status_code = 302)



