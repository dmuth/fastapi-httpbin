
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


from apis import methods
from apis import request

app = FastAPI(docs_url = "/", redoc_url = None,
    title = "FastAPI Httpbin",
    description = "A port of httpbin to the FastAPI framework.",
    version = "0.0.1",
    contact = {
        "name": "Douglas Muth",
        "url": "https://www.dmuth.org/",
        "email": "doug.muth@gmail.com"
        }
    )

app.include_router(methods.router)
app.include_router(request.router)


#
# TODO:
#
# X Write some unit tests
# X HTTP Methods: delete, patch, post, put
# X Figure out how to group endpoints in docs (tags?)
# X Make main page go to docs
# X Additional content on main page
#
# 1 Status Codes
# 2 Redirects
# 3 Anything
# Response Inspection
# Response formats
# Cookies
# Images
# Dynamic Data


# - Deploy to Deta


