#!/bin/bash
#
# Script to run the script in prod mode
#

# Errors are fatal
set -e

# Change to the parent directory
pushd $(dirname $0)/.. > /dev/null

echo "Running webserver on port 80..."

docker run --rm -p 80:80 fastapi-httpbin 

