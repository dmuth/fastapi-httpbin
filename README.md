
# FastAPI Httpbin


HTTP Endpoints for easy testing of your app.

Built with the [FastAPI Framework for Python](https://fastapi.tiangolo.com/), this is heavily based on the original [Httpbin](https://httpbin.org/) website.

Play with it in production at [https://httpbin.dmuth.org/[(https://httpbin.dmuth.org/)


## Differences between this app and Httpbin

- 100% unit test coverage of all endpoints.
- Ensured that documentation 100% matches the responses returned.
- Ensured that all values are now sanity checked
- All endpoints with mandatory parameters now have examples in the documentation in order to reduce friction for test usage.
- Fixed a few bugs found in the implementation of the `/cache` endpoints in Httpbin.
- Several endpoints have `GET` version only, as I did not see the point to supporting every possible HTTP verb--I felt that this just made the Swagger documentation unwieldly. (This is subject to change based on usage patters and demand)


## Development

To run FastAPI Httpbin in development mode so that changes to the underlying Python files
are automatically reloaded:

- Directly
  - `pip install -r ./requirements.txt`
  - `./bin/dev.sh` - Run server in dev mode, so that changes to the Python scripts cause them to be reloaded
  - `./pytest.sh` - Run all unit tests
- Or, in Docker if you'd prefer:
  - `./bin/docker-build.sh` - Build the Docker container
  - `./bin/docker-dev.sh` - Start the Docker container and spawn a bash shell so that scripts can be run


## In production

- `./bin/prod.sh` - Run in production mode, so that changes made to the Python scripts do NOT cause reloads.
- `./bin/docker-prod.sh` - Run the Docker container in production mode (detached from the console).


## Get In Touch

If you run into any problems, feel free to [open an issue](https://github.com/dmuth/fastapi-httpbin/issues).

Otherwise, you can find me [on Twitter](https://twitter.com/dmuth), [Facebook](https://facebook.com/dmuth), or drop me an email: **doug.muth AT gmail DOT com**.


