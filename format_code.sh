#!/bin/bash

for i in "$@"; do
  case $i in
    -rc=*|--rcfile=*)
      RCFILE="${i#*=}"
      shift
      ;;
    -*|--*)
      echo "Invalid option ${i%=*}" >&2
      exit 1
      ;;
  esac
done

if [ -z "$1" ]
    then
        black .
        pylint --output-format=colorized --rcfile="$RCFILE" \
            ./db/sc \
            ./db/tests \
            ./web/backend/service \
            ./web/backend/tests
    else
        black $1
        pylint --output-format=colorized --rcfile="$RCFILE" $1
fi

# Script for formatting code with black and linting it with pylint
#
# Script accepts:
#   * directory path
#   * path to rcfile for pylint provided with -rc or --rcfile argument name
# as optional inputs 