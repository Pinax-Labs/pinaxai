#!/bin/bash

############################################################################
# Format all libraries
# Usage: ./scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
PINAXAI_DIR="${REPO_ROOT}/libs/pinaxai"
PINAXAI_DOCKER_DIR="${REPO_ROOT}/libs/infra/pinaxai_docker"
PINAXAI_AWS_DIR="${REPO_ROOT}/libs/infra/pinaxai_aws"
COOKBOOK_DIR="${REPO_ROOT}/cookbook"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting all libraries"
source ${PINAXAI_DIR}/scripts/format.sh
source ${PINAXAI_DOCKER_DIR}/scripts/format.sh
source ${PINAXAI_AWS_DIR}/scripts/format.sh

# Format all cookbook examples
source ${COOKBOOK_DIR}/scripts/format.sh
