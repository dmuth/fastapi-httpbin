#!/bin/bash
#
# Run our app interactively, in development mode.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

LOCKFILE="uvicorn.pid"

FORCE=""
if test "$1" == "--force"
then
    FORCE=1
fi

PORT=${PORT:=8000}


#
# If we have a lockfile, check to see if the process is still running.
# The whole point to this code is that during development, I tried running this same
# script in different terminals one too many times, and got tired of dealing with that.
#
# The prod.sh script doesn't have any crazy logic like this.
#
if test -f ${LOCKFILE}
then
    PID=$(cat ${LOCKFILE})
    echo "# Lockfile ${LOCKFILE} found with PID ${PID}"

    FOUND=$(pgrep -F ${LOCKFILE} 2>/dev/null || true)

    if test "${FOUND}"
    then

        #
        # If the process was found, just bail out UNLESS --force was specified,
        # then we'll kill the existing process, wait for it to exit, and then continue here.
        #
        if test "${FORCE}"
        then
            echo "# PID ${PID} is still running, but --force was specified, so let's kill it."
            kill ${PID}

            while true
            do
                FOUND=$(pgrep -F ${LOCKFILE} 2>/dev/null || true)
                if test ! "${FOUND}"
                then
                    break
                fi
                echo "# Waiting for PID ${PID} to exit..."
                sleep 1

            done

        else
            echo "# PID ${PID} is still running, bailing out!"
            echo "# (Re-run with --force if you want to kill the running server and start one here.)"
            exit 1
        fi

    else
        echo "# ...but it was stale.  Continuing!"

    fi


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
uvicorn --host 0.0.0.0 main:app --reload --port ${PORT} &

PID=$!
echo "# Server process running as PID ${PID}."
echo ${PID} > ${LOCKFILE}


#
# Wait for the server to exit.
#
wait %1 2>/dev/null || true

#
# Wait once more, because if ctrl-C is received, execution of this bash script
# will continue while uvicorn shuts down.
#
wait %1 2>/dev/null || true

# Cleaning up
rm -f ${LOCKFILE}

echo "# Done!"

