
from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


from apis import methods
from apis import request
from apis import status
from apis import redirect
from apis import anything
from apis import response
from apis import response_formats
from apis import cookies
from apis import images
from apis import dynamic


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
        "name": "Responses",
        "description": "Inspect response data like caching and headers."
    },
    {
        "name": "Response Formats",
        "description": "Returns responses in different formats."
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
    {
        "name": "Cookies",
        "description": "Create, read, and delete cookies."
    },
    {
        "name": "Images",
        "description": "Return different image formats."
    },
    {
        "name": "Dynamic Data",
        "description": "Generate random and dynamic data."
    },
    ]

description = """
A port of httpbin to the FastAPI framework.<p/> 

<a href="/about">About this project</a> - 
<a href="https://github.com/dmuth/fastapi-httpbin">GitHub repo</a>

Run locally in Docker: <tt><b>docker run -p 80:80 dmuth1/fastapi-httpbin</b></tt>

"""

app = FastAPI(docs_url = "/", redoc_url = None,
    title = "FastAPI Httpbin",
    description = description,
    version = "0.0.1",
    swagger_ui_parameters = {"docExpansion":"none"},
    openapi_tags = tags_metadata
    )

app.include_router(methods.router, tags = ["HTTP Methods"])
app.include_router(status.router, tags = ["Status Codes"])
app.include_router(request.router, tags = ["Request Inspection"])
app.include_router(response.router, tags = ["Responses"])
app.include_router(response_formats.router, tags = ["Response Formats"])
app.include_router(redirect.router, tags = ["Redirects"])
app.include_router(anything.router, tags = ["Anything"])
app.include_router(cookies.router, tags = ["Cookies"])
app.include_router(images.router, tags = ["Images"])
app.include_router(dynamic.router, tags = ["Dynamic Data"])

app.mount("/about", StaticFiles(directory = "static/about", html = True), name = "static")


#
# TODO:
#
# k8s support through Minikube
#
# Uploads (10 MB max)
# Uploads with rate-limiting
#



