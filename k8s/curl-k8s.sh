#!/bin/bash
#
# Monitor our k8s cluster.
#

# Errors are fatal
set -e

echo localhost
curl -s localhost:8000/ip

#
# Remove newlines
#
function rm_newlines {
    tr -d "\n"
}

#
# Turn many spaces into a single one
#
function condense_space {
    sed -e 's/ \{1,\}/ /g'
}

echo httpbin
curl -s httpbin.localdomain:8000/ip | rm_newlines | condense_space
echo -e "\n"

echo httpbin2 
curl -s httpbin2.localdomain:8000/ip 2>&1 | rm_newlines | condense_space
echo -e "\n"

echo httpbin TLS
curl -ks https://httpbin.localdomain:8443/ip | rm_newlines | condense_space
echo -e "\n"

echo httpbin2 TLS
curl -ks https://httpbin2.localdomain:8443/ip | rm_newlines | condense_space
echo -e "\n"

