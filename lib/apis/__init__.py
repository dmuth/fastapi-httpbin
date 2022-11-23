
import json, typing
import logging

from fastapi import Query

from starlette.responses import Response


#
# Grab our logger out of Uvicorn so we can make use of it in our endpoints.
#
logger = logging.getLogger("uvicorn.error")
#logger.setLevel(logging.DEBUG)


#
# Set a response class that prettifies JSON.
# Borrowed from https://stackoverflow.com/a/69221989/196073
#
class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


#
# Our query parameters for our /redirect endpoints.
#
class RedirectQueryParams():

    def __init__(self,
        code: int | None = Query(
            default = 302, 
            description = "Status code passed in from a previous redirect", 
            example = 301)
        ):
        self.code = code


