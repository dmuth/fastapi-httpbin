
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

from lib.fastapi import tags_metadata, description

app = FastAPI(docs_url = "/", redoc_url = None,
    title = "FastAPI Httpbin",
    description = description,
    version = "0.0.5",
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
app.mount("/roadmap", StaticFiles(directory = "static/roadmap", html = True), name = "static")


