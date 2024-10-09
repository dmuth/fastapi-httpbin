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
# Actually make our image
#
def make_image(qr, transparent_background):

    # No transparent background?  No problem!
    if not transparent_background:
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        return(img)

    #
    # Transparent backgrounds are little more involved.
    # We'll have to go through each pixel, and change the background to be transparent.
    #
    img = qr.make_image(fill_color = 'black', back_color = 'white').convert('RGBA')

    data = img.getdata()

    new_data = []
    for item in data:
        # If the pixel is white, change it to transparent.  Otherwise, leave it alone.
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    # Update image data and return the image.
    img.putdata(new_data)

    return(img)

#
# Worker function to generate our QR Code.
#
def get_qr_code(url, box_size, border, transparent_background):

    #
    # Do some sanity checks
    #
    if box_size < 0:
        retval = {"type": "value_error.int.min_size", "message": f"Box_size {box_size} is < 0"}
        raise HTTPException(status_code = 422, detail = retval)

    elif border < 4:
        #
        # According to https://github.com/lincolnloop/python-qrcode, the minimum border is 4
        # according to the QR Code spec.
        #
        retval = {"type": "value_error.int.min_size", "message": f"Border {border} is < 4"}
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

    img = make_image(qr, transparent_background)

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
    box_size: int = Form(), 
    border: int = Form(),
    transparent_background: bool = Form(False),
    ):
    qrcode = get_qr_code(url, box_size, border, transparent_background)
    return Response(content = qrcode, media_type="image/png")


#
# Create our QRCode model.
# This is necessary so that the JSON is passed into the body.  Otherwise FastAPI
# will want the JSON to be passed in as GET-method data, even for a POST.  If that
# sounds weird, it's because it is.  That is maybe the sole issue I have with FastAPI.
#
class QRCode(BaseModel):
    url: str = Field(min_length = 10, max_length = 1000)
    box_size: int = Field(default = 10, gt = 0, le = 20)
    border: int = Field(default = 4, gt = 0, le = 20)
    transparent_background: bool = Form(False)
    
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
    transparent_background = data.transparent_background
    #print("Debugging", url, box_size, border, transparent_background) # Debugging
    qrcode = get_qr_code(url, box_size, border, transparent_background)
    return Response(content = qrcode, media_type="image/png")


#
# Set up our redirect.
#
@router.get("/qrcode", include_in_schema = False)
async def qrcode_get():
    return RedirectResponse(f"/qrcode/", status_code = 302)


#
# Commenting these out, because I don't think I'm actually using them with the latest revision.
#
#@router.post("/qr", include_in_schema = False)
#async def qr_post():
#    return RedirectResponse(f"/qrcode/", status_code = 302)
#
#
#@router.post("/qr-code", include_in_schema = False)
#async def qr_code_post():
#    return RedirectResponse(f"/qrcode/", status_code = 302)



