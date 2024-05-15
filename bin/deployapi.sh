#!/bin/bash
#
# Deploy out app to both Fly and build and push a Docker container.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null


echo "# "
echo "# Generating OpenAPI document..."
echo "# "
python3 extract-openapi.py main:app --out openapi.json

echo "# "
echo "# Pushing OpenAPI document to Docker Hub..."
echo "# "
oras push registry-1.docker.io/caroltyk/apis:fastapi-httpbin-$1 openapi.json:application/json