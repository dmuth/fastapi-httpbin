
import json, typing
import logging

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


