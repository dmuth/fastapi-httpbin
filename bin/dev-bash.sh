#!/bin/bash
#
# Spawn a bash shell in our dev container for debugging purposes
#

# Errors are fatal
set -e

# Change to the parent directory
pushd $(dirname $0)/.. > /dev/null

NAME="fastapi-httpbin-dev"

docker exec -it ${NAME} bash

