#!/bin/sh

# Errors are fatal
set -e

if test "$1"
then
        echo "# "
        echo "# Argument specified! Executing command: $@"
        echo "# "
        echo "# Run /mnt/bin/dev.sh' to start FastAPI in dev mode."
        echo "# "
        echo "# If you ran on the dev container, your host filesystem and code are in /mnt/."
        echo "# "
        exec $@
fi

cd /mnt

/app/bin/prod.sh

