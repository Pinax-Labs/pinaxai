#!/bin/bash

############################################################################
# Format the pinaxai library using ruff
# Usage: ./libs/pinaxai/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting pinaxai"

print_heading "Running: ruff format ${PINAXAI_DIR}"
ruff format ${PINAXAI_DIR}

print_heading "Running: ruff check --select I --fix ${PINAXAI_DIR}"
ruff check --select I --fix ${PINAXAI_DIR}
