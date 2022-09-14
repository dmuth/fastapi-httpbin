#
# All responses.
#

import re

from fastapi import APIRouter, Query, Body
from fastapi import FastAPI, Header, Request, Response, HTTPException
from fastapi.responses import PlainTextResponse, HTMLResponse

from . import PrettyJSONResponse

router = APIRouter()


@router.get("/html", response_class = HTMLResponse,
    summary = "Returns an HTML document.")
async def html(response: Response):

    retval = """
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
      <h1>FastAPI Httpbin HTMLResponse</h1>

      <div>
        <p>
            This is a sample HTML response.
        </p>
      </div>
  </body>
</html>
"""

    return(retval)


@router.get("/json", summary = "Returns a JSON document.",
    response_class=PrettyJSONResponse)
async def json(response: Response):

    retval = {
        "title": "Undertale Soundtrack",
        "author": "Toby Fox",
        "tracks": [
            "Once Upon a Time",
            "Your Best Friend",
            "Fallen Down",
            "Enemy Approaching",
            "Determination",
            "Nyeh Heh Heh!",
            "Dogsong",
            "Snowdin Town",
            "Bonetrousle",
            "Quiet Water",
            "Temmie Village",
            "Spear of Justice",
            "Spider Dance",
            "It's Raining Somewhere Else",
            "CORE",
            "Death by Glamour",
            "The Choice",
            "Your Best Nightmare",
            "Finale",
            "An Ending",
            "Fallen Down (Reprise)",
            "Don't Give Up",
            "Hopes and Dreams",
            "Reunited",
            "Last Goodbye"
            ],
        "urls": [
            "https://en.wikipedia.org/wiki/Undertale_Soundtrack",
            "https://www.youtube.com/watch?v=tz82xbLvK_k&list=OLAK5uy_l6pEkEJgy577R-aDlJ3Gkp5rmlgIOu8bc&index=87"
            ]
        }

    return(retval)


@router.get("/robots.txt", summary = "Returns some robots.txt rules.")
async def robots_txt(response: Response):

    retval = """
User-agent: *
Disallow: /deny
"""
    return Response(retval, media_type = "text/plain")


@router.get("/deny", summary = "Returns a page denied by rules in robots.txt.")
async def deny(response: Response):

    retval = """
░░░░░░░░░░░░░░░░░░░░
░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░

You pet the Dog. Its excitement knows no bounds.
"""
    return Response(retval, media_type = "text/plain")


@router.get("/xml", summary = "Returns an XML document")
async def xml(response: Response):

    retval = """
        <?xml version='1.0' encoding='us-ascii'?>
        <title>Undertale Soundtrack</title>
        <author>Toby Fox</author>
        <tracks>
            <track>Once Upon a Time</track>
            <track>Your Best Friend</track>
            <track>Fallen Down</track>
            <track>Enemy Approaching</track>
            <track>Determination</track>
            <track>Nyeh Heh Heh!</track>
            <track>Dogsong</track>
            <track>Snowdin Town</track>
            <track>Bonetrousle</track>
            <track>Quiet Water</track>
            <track>Temmie Village</track>
            <track>Spear of Justice</track>
            <track>Spider Dance</track>
            <track>It's Raining Somewhere Else</track>
            <track>CORE</track>
            <track>Death by Glamour</track>
            <track>The Choice</track>
            <track>Your Best Nightmare</track>
            <track>Finale</track>
            <track>An Ending</track>
            <track>Fallen Down (Reprise)</track>
            <track>Don't Give Up</track>
            <track>Hopes and Dreams</track>
            <track>Reunited</track>
            <track>Last Goodbye</track>
        </tracks>
        <url>https://en.wikipedia.org/wiki/Undertale_Soundtrack</url>
"""

    return Response(retval, media_type = "application/xml ")


@router.get("/encoding/utf8", summary = "Returns a UTF-8 Encoded body.")
async def utf8(response: Response):

    retval = ""

    with open("private/utf8.txt") as f:
        lines = f.readlines()

    retval = "".join(lines)

    return Response(retval, media_type = "text/plain")



