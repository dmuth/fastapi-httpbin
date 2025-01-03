#
# Yahtzee endpoint
#

from io import BytesIO
import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException, Form, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

router = APIRouter()


@router.post("/yahtzee/form", summary = "Analyzes a Yahtzee dice roll"
    )
async def yahtzee_post_form(
    ):
    retval = {}
    print("TEST", router.state.persistent_data)
    return(retval)


#
# Set up our redirect.
#
@router.get("/yahtzee", include_in_schema = False)
async def yahtzee_get():
    return RedirectResponse(f"/yahtzee/", status_code = 302)


