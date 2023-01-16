#
# All requests
#

import json

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

from lib.fastapi import tags_metadata, description, app_version

from . import logger
from . import PrettyJSONResponse

router = APIRouter()


@router.get("/version", summary = "The version of this app.",
    response_class=PrettyJSONResponse)
async def version(request: Request):

    retval = {}
    retval["version"] = app_version

    return(retval)


