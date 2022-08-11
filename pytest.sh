#!/bin/bash
#
# Run our unit tests
#

# Chagne to the directory where this script lives
pushd $(dirname $0) > /dev/null

python3 -m pytest -s

