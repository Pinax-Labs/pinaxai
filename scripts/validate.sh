#!/bin/bash

############################################################################
# Validate all libraries
# Usage: ./scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
PINAXAI_DIR="${REPO_ROOT}/libs/pinaxai"
PINAXAI_DOCKER_DIR="${REPO_ROOT}/libs/infra/pinaxai_docker"
PINAXAI_AWS_DIR="${REPO_ROOT}/libs/infra/pinaxai_aws"
source ${CURR_DIR}/_utils.sh

print_heading "Validating all libraries"
source ${PINAXAI_DIR}/scripts/validate.sh
source ${PINAXAI_DOCKER_DIR}/scripts/validate.sh
source ${PINAXAI_AWS_DIR}/scripts/validate.sh
