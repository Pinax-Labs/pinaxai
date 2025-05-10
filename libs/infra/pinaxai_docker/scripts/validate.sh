#!/bin/bash

############################################################################
# Validate the pinaxai_docker library using ruff and mypy
# Usage: ./libs/infra/pinaxai_docker/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating pinaxai_docker"

print_heading "Running: ruff check ${PINAXAI_DOCKER_DIR}"
ruff check ${PINAXAI_DOCKER_DIR}

print_heading "Running: mypy ${PINAXAI_DOCKER_DIR} --config-file ${PINAXAI_DOCKER_DIR}/pyproject.toml"
mypy ${PINAXAI_DOCKER_DIR} --config-file ${PINAXAI_DOCKER_DIR}/pyproject.toml
