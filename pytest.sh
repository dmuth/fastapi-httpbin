#!/bin/bash
#
# Run our unit tests
#

# Errors are fatal
set -e

# Change to the directory where this script lives
pushd $(dirname $0) > /dev/null

echo "# "
echo "# Running unit tests..."
echo "# "
echo "# If you want to run specific tests, try: "
echo "# "
echo "# $0 -k PATTERN"
echo "# "

#
# The reason we're checking for an argument here is because if we don't,
# Pytest will "helpfully" scan for all files starting with "test_", which will
# include file in lib/, which is obviously not a test.
#
TESTS=""
if ! test "$@"
then
    TESTS="./tests"
fi

python3 -m pytest -s ${TESTS} $@

