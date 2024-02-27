#!/bin/bash

# Directory to start from
start_dir="$1"

# Check if the start directory is provided
if [ -z "$start_dir" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Find and convert all .eps files to .png
find "$start_dir" -type f -name '*.eps' -exec sh -c '
for file; do
    # Replace the file extension from .eps to .png
    png="${file%.eps}.png"
    
    # Convert the file
    echo "Converting $file to $png"
    convert "$file" "$png"
done
' sh {} +