
#!/usr/bin/env bash

set -eo pipefail

./scripts/run_bootstrap.sh

python3 -m unittest discover -v tests