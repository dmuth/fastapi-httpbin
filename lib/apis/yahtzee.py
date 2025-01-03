#
# Yahtzee endpoint
#

from io import BytesIO
import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

router = APIRouter()



@router.post("/yahtzee/form", summary = "Analyzes a Yahtzee dice roll",
    response_class=Response
    )
async def yahtzee_post_form(url: str = Form(),
    box_size: int = Form(), 
    border: int = Form(),
    transparent_background: bool = Form(False),
    ):
    retval = {}
    return retval


#
# Set up our redirect.
#
@router.get("/yahtzee", include_in_schema = False)
async def yahtzee_get():
    return RedirectResponse(f"/yahtzee/", status_code = 302)


