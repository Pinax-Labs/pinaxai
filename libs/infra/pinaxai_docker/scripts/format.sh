#!/bin/bash

############################################################################
# Format the pinaxai_docker library using ruff
# Usage: ./libs/infra/pinaxai_docker/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting pinaxai_docker"

print_heading "Running: ruff format ${PINAXAI_DOCKER_DIR}"
ruff format ${PINAXAI_DOCKER_DIR}

print_heading "Running: ruff check --select I --fix ${PINAXAI_DOCKER_DIR}"
ruff check --select I --fix ${PINAXAI_DOCKER_DIR}
