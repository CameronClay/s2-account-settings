#!/bin/bash
# should be called from scripts directory

SOURCE_DIR=$(dirname "${BASH_SOURCE[0]}")
source $SOURCE_DIR"/vars.sh"

MSG=$(python ../s2-settings.py -k -v "$sc_dir")
echo $MSG
