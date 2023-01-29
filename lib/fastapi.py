
#
# Store our app version here.
#
app_version = "0.0.40"

tags_metadata = [
    {
        "name": "HTTP Methods",
        "description": "Testing different HTTP verbs."
    },
    {
        "name": "Request Inspection",
        "description": "Inspect the request data. (including source IP address)"
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
        "name": "QR Codes",
        "description": "Generate QR Codes."
    },
    {
        "name": "Dynamic Data",
        "description": "Generate random and dynamic data."
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
        "name": "Forms",
        "description": "Endpoints for testing out forms."
    },
    {
        "name": "Meta",
        "description": "Endpoints related to this app itself."
    },
    ]


description = """
<a href="static/logo.png"><img src="static/logo.png" align="right" /></a>

HTTP Endpoints for easy testing of your app.

Built with the <a href="https://fastapi.tiangolo.com/">FastAPI framework</a>, 
this is heavily based on the original <a href="https://httpbin.org/">Httpbin</a> website.

<a href="/about">About this project</a> - 
<a href="/roadmap">Development Roadmap</a> -
<a href="/qrcode/">Dead Simple QR Code Generator</a> -
<a href="/test-password-manager-form/">Form for testing Password Managers like 1Password and BitWarden</a>
<p>

<a href="https://github.com/dmuth/fastapi-httpbin">GitHub repo</a>
<p>

Run locally in Docker: <tt><b>docker run -p 80:80 dmuth1/fastapi-httpbin</b></tt>

<a href="https://httpbin.dmuth.org/">Main Site</a> - Mirrors: 
<a href="https://fly.httpbin.dmuth.org/">Fly</a>
<a href="https://railway.httpbin.dmuth.org/">Railway</a>
<a href="https://render.httpbin.dmuth.org/">Render</a>

"""


