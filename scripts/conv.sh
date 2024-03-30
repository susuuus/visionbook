#!/bin/bash

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

# TEMP_TEX="${input_file%.tex}-temp.tex" # Create a temp file name based on the input file

# sed -i 's/\\marginnote{\(.*\)}/::: {\.column-margin}\n\1\n:::/g' $TEMP_TEX
# sed -E "s/\\marginnote\{([^\}]*)\}/::: {.column-margin}\n\1\n:::/g" "$input_file" > "$TEMP_TEX"

# Run Pandoc conversion
pandoc "$input_file" -o "$output_file" -f latex  -t markdown --filter $SCRIPT_DIR/filter.py

echo "Conversion completed: $output_file"

# remove the [x in] or [x pt]
# sed -i '' -E 's/\\\[\-?\([0-9]*\)\(\.[0-9]+\)\?\(in\|cm\|pt\)\\\]//g' "$output_file"
sed -i '' -E 's/\\\[[-]?[0-9]+(\.[0-9]+)?(in|cm|pt)\\\]//g' "$output_file"