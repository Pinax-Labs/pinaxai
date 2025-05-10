#!/bin/bash

############################################################################
# Validate the pinaxai library using ruff and mypy
# Usage: ./libs/pinaxai/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating pinaxai"

print_heading "Running: ruff check ${PINAXAI_DIR}"
ruff check ${PINAXAI_DIR}

print_heading "Running: mypy ${PINAXAI_DIR} --config-file ${PINAXAI_DIR}/pyproject.toml"
mypy ${PINAXAI_DIR} --config-file ${PINAXAI_DIR}/pyproject.toml
