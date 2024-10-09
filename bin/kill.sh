#!/bin/bash
#
# Kill our containers
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

echo "# Killing Docker container(s)..."
docker ps | grep fastapi-httpbin | awk '{print $1}' | xargs docker kill

echo "# OK: Done!"

