#!/bin/bash
#
# Monitor our k8s cluster.
#

# Errors are fatal
set -e

watch -d -n1 "kubectl get nodes,all"

