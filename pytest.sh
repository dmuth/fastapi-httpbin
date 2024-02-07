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

#
# We have to ignore deprecation warnings because it looks like the Swagger module
# hasn't yet caught up with Pydantic wanting "examples" instead of "example".
# Once Swagger is updated, I'll fix my code and stop ignoring deprecation warnings.
#
#python3 -m pytest -s ${TESTS} $@
python3 -m pytest -W ignore::DeprecationWarning -s ${TESTS} $@ 

