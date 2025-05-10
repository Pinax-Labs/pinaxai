#!/bin/bash

############################################################################
# Run tests for the pinaxai library
# Usage: ./libs/pinaxai/scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests for pinaxai"

print_heading "Running: pytest ${PINAXAI_DIR} with coverage"
pytest ${PINAXAI_DIR}/tests/unit --cov=${PINAXAI_DIR}/pinaxai --cov-report=term-missing --cov-report=html
