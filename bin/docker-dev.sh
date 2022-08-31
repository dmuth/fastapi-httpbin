#!/bin/bash
#
# Script to run the script in dev mode, which will spawn a shell
#

# Errors are fatal
set -e

# Change to the parent directory
pushd $(dirname $0)/.. > /dev/null

docker run --rm -it -e PORT=8000 -p 8000:8000 -v $(pwd):/mnt fastapi-httpbin bash


