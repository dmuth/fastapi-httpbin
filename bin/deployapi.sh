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
api_id=$(curl --location --request POST 'http://tyk-dashboard.org/api/apis/oas/import' \
  --header 'Authorization: e2f234ac32ab443e78962ef941898722' \
  --header 'Content-Type: text/plain' \
  --data-raw $body | jq -r '.ID')
sleep 1

echo "# "
echo "# Temporary API ID $api_id ..."
echo "# "
sleep 1

echo "# "
echo "# Retrieve API Definition JSON..."
echo "# "
curl --location --request GET 'http://tyk-dashboard.org/api/apis/oas/$api_id' \
  --header 'Authorization: e2f234ac32ab443e78962ef941898722' \
  --header 'Content-Type: text/plain' > apidefinition.json
sleep 1

echo "# "
echo "# Pushing API Definition to Docker Hub..."
echo "# "
oras push registry-1.docker.io/caroltyk/apis:fastapi-httpbin-$1 apidefinition.json:application/json