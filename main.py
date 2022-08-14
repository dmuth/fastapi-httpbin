
from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel


from apis import methods
from apis import request
from apis import status
from apis import redirect
from apis import anything


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
app.include_router(redirect.router)
app.include_router(anything.router)


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
# 3 /get - update syntax diagram to include GET method data!
#
# 2 Content on main page: add a link to GitHub
#
# 3 prod script
#
# Docker image with dev and prod scripts and requirements.txt
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



