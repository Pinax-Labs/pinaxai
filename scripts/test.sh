#!/bin/bash

############################################################################
# Run tests for all libraries
# Usage: ./scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
PINAXAI_DIR="${REPO_ROOT}/libs/pinaxai"
PINAXAI_DOCKER_DIR="${REPO_ROOT}/libs/infra/pinaxai_docker"
PINAXAI_AWS_DIR="${REPO_ROOT}/libs/infra/pinaxai_aws"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests with coverage for all libraries"

# Run tests with coverage for each library
source ${PINAXAI_DOCKER_DIR}/scripts/test.sh
source ${PINAXAI_AWS_DIR}/scripts/test.sh
source ${PINAXAI_DIR}/scripts/test.sh

# Combine coverage reports (optional)
coverage combine
coverage report
coverage html -d coverage_report
