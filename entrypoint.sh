#!/bin/bash

set -e

echo "Starting setup ..."

source /opt/ros/jazzy/setup.bash
source install/setup.bash

echo "Setup finished"
echo "Launching nodes ..."

exec "$@"