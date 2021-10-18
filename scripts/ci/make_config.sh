#!/usr/bin/env bash

set -eo pipefail

rm -f $1

echo "
[db]
name = sc
uri = bolt://localhost:7687
user = neo4j
password = $2
" >> $1 
