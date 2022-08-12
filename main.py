
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


from apis import methods
from apis import request

app = FastAPI()
app.include_router(methods.router)
app.include_router(request.router)


#
# TODO:
#
# X Write some unit tests
#X HTTP Methods: delete, patch, post, put
# X Figure out how to group endpoints in docs (tags?)
#
# 1 Make main page go to docs
# 2 Additional content on main page
#
# Status Codes
# Redirects
# Response Inspection
# Response formats
# Dynamic Data
# Cookies
# Images
# Anything


# - Deploy to Deta


