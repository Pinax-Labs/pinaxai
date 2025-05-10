#!/bin/bash

############################################################################
# Release pinaxai to pypi
# Usage: ./libs/pinaxai/scripts/release_manual.sh
# Note:
#   build & twine must be available in the venv
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PINAXAI_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Releasing *pinaxai*"

  cd ${PINAXAI_DIR}
  print_heading "pwd: $(pwd)"

  print_heading "Proceed?"
  space_to_continue

  print_heading "Building pinaxai"
  python3 -m build

  print_heading "Release pinaxai to testpypi?"
  space_to_continue
  python3 -m twine upload --repository testpypi ${PINAXAI_DIR}/dist/*

  print_heading "Release pinaxai to pypi"
  space_to_continue
  python3 -m twine upload --repository pypi ${PINAXAI_DIR}/dist/*
}

main "$@"
