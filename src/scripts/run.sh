#!/bin/bash
# should be called from scripts directory

SOURCE_DIR=$(dirname "${BASH_SOURCE[0]}")
source $SOURCE_DIR"/vars.sh"

MSG=$(cd .. && python -m s2_settings -k -v "$sc_dir")
echo $MSG
