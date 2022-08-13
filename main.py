
from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel


from apis import methods
from apis import request
from apis import status

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
app.include_router(status.router)


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
# 1 Status Codes
# 2 Redirects
# 3 Anything
# Content on main page: add a link to GitHub
# prod script
# Docker image with dev and prod scripts and requirements.txt
# Response Inspection
# Response formats
# Cookies
# Images
# Dynamic Data
# k8s support through Minikube
# Uploads (10 MB max)
# Uploads with rate-limiting

# - Deploy to Deta



