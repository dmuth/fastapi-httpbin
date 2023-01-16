#
# All requests
#

import json

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

import config

from . import logger
from . import PrettyJSONResponse

router = APIRouter()

app_version = config.app_version


@router.get("/version", summary = "The version of this app.",
    response_class=PrettyJSONResponse)
async def version(request: Request):

    retval = {}
    retval["version"] = app_version

    return(retval)


