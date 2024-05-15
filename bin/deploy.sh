#!/bin/bash
#
# Deploy out app to both Fly and build and push a Docker container.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

if test "$1"
then
    tag=$1
else
    tag=latest
fi


echo "# "
echo "# Building Docker image..."
echo "# "
./bin/docker-build.sh

echo "# "
echo "# Pushing Docker image to Docker Hub..."
echo "# "
./bin/docker-push.sh $tag

#echo "# "
#echo "# Deploying to Fly.io..."
#echo "# "
#fly deploy

./bin/deployapi.sh $tag

echo "# Done!"

