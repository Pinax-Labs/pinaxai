#!/bin/bash

############################################################################
# Format the pinaxai_aws library using ruff
# Usage: ./libs/infra/pinaxai_aws/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_AWS_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting pinaxai_aws"

print_heading "Running: ruff format ${PINAXAI_AWS_DIR}"
ruff format ${PINAXAI_AWS_DIR}

print_heading "Running: ruff check --select I --fix ${PINAXAI_AWS_DIR}"
ruff check --select I --fix ${PINAXAI_AWS_DIR}
