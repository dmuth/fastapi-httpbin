#!/bin/bash
#
# Run our app interactively, in development mode.
#

# Errors are fatal
set -e

LOCKFILE="uvicorn.pid"

# Chagne to the directory where this script lives
pushd $(dirname $0) > /dev/null

if test -f ${LOCKFILE}
then
    PID=$(cat ${LOCKFILE})
    echo "LOCKFILE FOUND with PID ${PID}"

    FOUND=$(pgrep -F ${LOCKFILE} || true)

    if test "${FOUND}"
    then
        echo "PID ${PID} is still running, bailing out!"
        exit
    fi

    echo "# ...but it was stale.  Continuing!"

fi


#
# Handler for when a kill signal is received.
# An attempt to kill the server will be made, in case this script is killed via SIGTERM.
#
function signal_received() {
    echo "# ctrl-C or kill signal received, bailing!"
    kill ${PID} || true
}

trap signal_received INT TERM


#
# Run the main app and get the PID
#
uvicorn main:app --reload &

PID=$!
echo "# Server process running as PID ${PID}."
echo ${PID} > ${LOCKFILE}


#
# Wait for the server to exit.
#
wait %1 || true

#
# Wait once more, because if ctrl-C is received, execution of this bash script
# will continue while uvicorn shuts down.
#
wait %1 || true

# Cleaning up
rm -f ${LOCKFILE}

echo "# Done!"

