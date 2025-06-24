#!/bin/bash

# Start directory is grandparent/figures
start_dir="$(dirname "$(dirname "$PWD")")/figures"

# Find and convert all .pdf files to .png with high resolution
find "$start_dir" -type f -name '*.pdf' -exec sh -c '
for file; do
    # Replace the file extension from .pdf to .png
    png="${file%.pdf}.png"
    echo "Converting $file to $png with high resolution and trimming transparent background"
    convert -density 300 "$file" -quality 100 -trim "$png"

done
' sh {} +
