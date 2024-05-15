#!/bin/bash
#
# Deploy app to build and push a Docker container.
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
echo "# Converting to Tyk OAS API Definition..."
echo "# "
body=$(<openapi.json)
wget --method=POST http://tyk-dashboard.org/api/apis/oas/import --header='Authorization: e2f234ac32ab443e78962ef941898722' --header='Content-Type: text/plain' --body-data="$body" -O res.json
api_id=$(cat res.json | jq -r '.ID')

echo "# "
echo "# Temporary API ID $api_id ..."
echo "# "

echo "# "
echo "# Retrieve API Definition JSON..."
echo "# "
wget --method=GET http://tyk-dashboard.org/api/apis/oas/$api_id --header 'Authorization: e2f234ac32ab443e78962ef941898722' --header 'Content-Type: text/plain' -O apidefinition.json


echo "# "
echo "# Remove Temporary API $api_id ..."
echo "# "
wget --method=DELETE http://tyk-dashboard.org/api/apis/oas/$api_id --header 'Authorization: e2f234ac32ab443e78962ef941898722' -O deleteres.json

rm res.json
rm deleteres.json

echo "# "
echo "# Pushing API Definition to Docker Hub..."
echo "# "
oras push registry-1.docker.io/caroltyk/apis:fastapi-httpbin-$1 apidefinition.json:application/json