#!/bin/bash
#
# Run our app interactively, in development mode.
#

# Errors are fatal
set -e

PORT=${PORT:=8000}

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

#
# Run the main app
#
uvicorn --host 0.0.0.0 --port ${PORT} main:app


