#!/bin/bash
#
# Deploy out app to both Fly and build and push a Docker container.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null


echo "# "
echo "# Deploying to Fly.io..."
echo "# "
fly deploy

echo "# "
echo "# Building Docker image..."
echo "# "
./bin/docker-build.sh

echo "# "
echo "# Pushing Docker image..."
echo "# "
./bin/docker-push.sh

echo "# Done!"

