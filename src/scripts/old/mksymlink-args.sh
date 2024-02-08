#!/bin/bash

source_dir="$(pwd)"
argc=$#

if [ $argc -lt 1 ]; then
	echo "Expected SC2 Documents Directory"
	exit 1
fi

echo "argc="$argc", source_dir=""$source_dir"

target_dir="$1"
echo "target_dir=""$target_dir"

echo ""

MSG=$(ln -s "$source_dir"/ "$target_dir")

if [ $? != "" ]; then
	echo ""
    	echo $MSG
fi
