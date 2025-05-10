#!/bin/bash

############################################################################
# Validate the pinaxai_aws library using ruff and mypy
# Usage: ./libs/infra/pinaxai_aws/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_AWS_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating pinaxai_aws"

print_heading "Running: ruff check ${PINAXAI_AWS_DIR}"
ruff check ${PINAXAI_AWS_DIR}

print_heading "Running: mypy ${PINAXAI_AWS_DIR} --config-file ${PINAXAI_AWS_DIR}/pyproject.toml"
mypy ${PINAXAI_AWS_DIR} --config-file ${PINAXAI_AWS_DIR}/pyproject.toml
