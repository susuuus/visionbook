#!/bin/bash

# Directory to start from
start_dir="$1"

# Check if the start directory is provided
if [ -z "$start_dir" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Find and convert all .pdf files to .png
find "$start_dir" -type f -name '*.pdf' -exec sh -c '
for file; do
    # Replace the file extension from .pdf to .png
    png="${file%.pdf}.png"
    
    # Convert the file
    echo "Converting $file to $png"
    convert "$file" "$png"
done
' sh {} +