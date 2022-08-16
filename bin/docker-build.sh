#!/bin/bash
#
# Build our Docker image.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

docker build -t fastapi-httpbin . -f ./Dockerfile


