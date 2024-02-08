#!/bin/bash
# should be called from scripts directory

SOURCE_DIR=$(dirname "${BASH_SOURCE[0]}")
source $SOURCE_DIR"/vars.sh"

source_dir="$(pwd)"
target_dir="$sc_dir"
echo "source_dir=""$source_dir"", ""target_dir=""$target_dir"

echo ""

MSG=$(ln -s "$source_dir"/ "$target_dir")

if [ $? != "" ]; then
	echo ""
    	echo $MSG
fi
