#!/bin/bash
#
# Run our app interactively, in development mode.
#

# Chagne to the directory where this script lives
pushd $(dirname $0) > /dev/null

uvicorn main:app --reload


