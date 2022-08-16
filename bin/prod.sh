#!/bin/bash
#
# Run our app interactively, in development mode.
#

# Errors are fatal
set -e

# Change to the directory where this script lives
pushd $(dirname $0) > /dev/null

#
# Run the main app
#
uvicorn main:app


