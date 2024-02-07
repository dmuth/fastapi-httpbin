#!/bin/bash
#
# Script to run the script in dev mode, which will spawn a shell
#

# Errors are fatal
set -e

# Change to the parent directory
pushd $(dirname $0)/.. > /dev/null

PORT=${PORT:=8000}

docker run --rm -it -e PORT=${PORT} -p ${PORT}:${PORT} \
    --name fastapi-httpbin-dev \
    -v $(pwd):/mnt fastapi-httpbin bash

