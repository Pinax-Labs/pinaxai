#!/bin/bash

############################################################################
# Run tests for the pinaxai library
# Usage: ./libs/infra/pinaxai_docker/scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests for pinaxai"

print_heading "Running: pytest ${PINAXAI_DOCKER_DIR}"
pytest ${PINAXAI_DOCKER_DIR}/tests
