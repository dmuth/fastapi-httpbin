
from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel


from apis import methods
from apis import request
from apis import status
from apis import redirect
from apis import anything


tags_metadata = [
    {
        "name": "HTTP Methods",
        "description": "Testing different HTTP verbs."
    },
    {
        "name": "Request Inspection",
        "description": "Inspect the request data."
    },
    {
        "name": "Status Codes",
        "description": "Generate responses with specified status codes."
    },
    {
        "name": "Redirects",
        "description": "Return different redirects."
    },
    {
        "name": "Anything",
        "description": "Return anything that is passed in on the request."
    },
    ]

description = """
A port of httpbin to the FastAPI framework.<p/> 

<a href="https://github.com/dmuth/fastapi-httpbin">GitHub repo</a>

"""

app = FastAPI(docs_url = "/", redoc_url = None,
    title = "FastAPI Httpbin",
    description = description,
    version = "0.0.1",
    contact = {
        "name": "Douglas Muth",
        "url": "https://www.dmuth.org/",
        "email": "doug.muth@gmail.com"
        },
    swagger_ui_parameters = {"docExpansion":"none"},
    openapi_tags = tags_metadata
    )

app.include_router(methods.router, tags = ["HTTP Methods"])
app.include_router(request.router, tags = ["Request Inspection"])
app.include_router(status.router, tags = ["Status Codes"])
app.include_router(redirect.router, tags = ["Redirects"])
app.include_router(anything.router, tags = ["Anything"])


#
# TODO:
#
# X Write some unit tests
# X HTTP Methods: delete, patch, post, put
# X Figure out how to group endpoints in docs (tags?)
# X Make main page go to docs
# X Additional content on main page
#
# X dev script: Add in process tracking
# X Status Codes
# X Redirects
# X Anything - include method and args
#   Also "data" for POST method data!
#   Unit test for post data
# X Reorder HTTP verbs for consistency
# X Go back and figure out POST method data, return as "data" in POST endpoint
# X Descriptions for tags
# X Keep tags closed by default
# X Content on main page: add a link to GitHub
#
# 1 prod script
# 2 Docker image with dev and prod scripts and requirements.txt
#   - Move scripts into bin/
#
# GitHub: Add README, include testing info with Docker
#
# Response Inspection
# Response formats
# Cookies
# Images
# Dynamic Data
# k8s support through Minikube
# Uploads (10 MB max)
# Uploads with rate-limiting

# - Deploy to Deta



