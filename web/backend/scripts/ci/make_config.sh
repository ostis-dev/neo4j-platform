#!/usr/bin/env bash

set -eo pipefail

rm -f $1

echo "
[tornado]
cookie_secret = test_secret

[sc]
config = ${CONFIG_PATH_TO_SC_CONFIG}
" >> $1 
