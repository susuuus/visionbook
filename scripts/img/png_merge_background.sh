#!/bin/bash

# Directory to start from
start_dir="$1"

# Check if the start directory is provided
if [ -z "$start_dir" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

find "$start_dir" -type f -name '*.png' -exec sh -c '
for file; do
    convert -density 300 "$file" -background white -flatten -resize 1024x1024 -alpha remove "$file"
done
' sh {} +