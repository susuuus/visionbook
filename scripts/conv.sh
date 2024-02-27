#!/bin/bash

# Check if an input file was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 /path/to/file.tex"
    exit 1
fi

SCRIPT_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
echo $SCRIPT_DIR
input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file does not exist: $input_file"
    exit 1
fi

# Extract the directory, filename without extension, and extension
dir=$(dirname "$input_file")
base_name=$(basename "$input_file" .tex)

# Set the output file path
output_file="${base_name}.qmd"

# Run Pandoc conversion
pandoc "$input_file" -o "$output_file" -f latex -t markdown --filter $SCRIPT_DIR/filter.py

echo "Conversion completed: $output_file"