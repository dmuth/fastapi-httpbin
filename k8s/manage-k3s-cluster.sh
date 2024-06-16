#!/bin/bash
#
# Used to stand up and tear down k3d clusters.
#

# Errors are fatal
set -e

ACTION=""
NODES=3
AGENTS=$(( NODES - 1 ))
#PORTS="-p 8081:80@loadbalancer -p 8082:30080@agent:0"
#PORTS="-p 8080:80@loadbalancer -p 8443:443@loadbalancer -p 8081:30080@agent:0"
PORTS="-p 8000:80@loadbalancer -p 8080:80@loadbalancer -p 8443:443@loadbalancer -p 8081:30080@agent:0"

#
# Print our syntax and exit.
#
function print_syntax() {

    echo "! "
    echo "! Syntax: $0 ( list | create | delete | create-force )"
    echo "! "
    echo "! list - List k3s clusters"
    echo "! create - Creates a k3s cluster"
    echo "! delete - Deletes the cluster if it exists"
    echo "! create-force - Creates a k3s cluster, deleting one if it already exists."
    echo "! "
    exit 1

} # End of print_syntax()


#
# Parse our args.
#
function parse_args() {

    if test ! "$1"
    then
        print_syntax
    fi

    if test "$1" == "-h" -o "$1" == "--help"
    then
        print_syntax
    fi

    if test "$1" == "list"
    then
        ACTION="list"

    elif test "$1" == "create"
    then
        ACTION="create"

    elif test "$1" == "delete"
    then
        ACTION="delete"

    elif test "$1" == "create-force"
    then
        ACTION="create-force"

    else 
        print_syntax

    fi

} # End of parse_args()


#
# Import images from our parent Docker instance.
#
function import_images() {

    echo "# "
    echo "# Importing httpbin image..."
    echo "# "
    k3d image import dmuth1/fastapi-httpbin

} # End of import_images()


parse_args $@

if test "${ACTION}" == "list"
then
    echo "# "
    echo "# k3s clusters:"
    echo "# "
    k3d cluster list

elif test "${ACTION}" == "create"
then
true
    echo "# "
    echo "# Creating k3s cluster..."
    echo "# "
    echo "# Nodes: ${NODES}"
    echo "# Ports: ${PORTS}"
    echo "# "
    k3d cluster create --agents ${AGENTS} ${PORTS}
    import_images

elif test "${ACTION}" == "delete"
then
true
    echo "# "
    echo "# Deleting k3s cluster..."
    echo "# "
    k3d cluster delete

elif test "${ACTION}" == "create-force"
then
true

    echo "# "
    echo "# First, deleting cluster..."
    echo "# "
    k3d cluster delete

    echo "# "
    echo "# Now re-creating cluster..."
    echo "# "
    echo "# Nodes: ${NODES}"
    echo "# Ports: ${PORTS}"
    echo "# "
    k3d cluster create --agents ${AGENTS} ${PORTS}
    import_images

fi

echo "# OK: Done!"

