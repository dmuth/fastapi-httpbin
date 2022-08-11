

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

router = APIRouter()


@router.get("/get")
async def get(request: Request):

	retval = {}

	retval["args"] = request.query_params
	retval["headers"] = request.headers
	retval["source"] = {
		"ip": request.client[0],
		"port": request.client[1]
		}
	retval["url"] = request.url

	return(retval)


