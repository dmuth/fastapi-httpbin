#!/bin/bash
#
# Run our unit tests
#

echo "# "
echo "# Running unit tests..."
echo "# "
echo "# If you want to run specific tests, try: "
echo "# "
echo "# $0 -k PATTERN"
echo "# "

# Chagne to the directory where this script lives
pushd $(dirname $0) > /dev/null

python3 -m pytest -s $@

