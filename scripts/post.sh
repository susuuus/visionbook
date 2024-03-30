
#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
echo $SCRIPT_DIR
input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file does not exist: $input_file"
    exit 1
fi


sed -i '' -E 's/\\\[[-]?[0-9]*\.?[0-9]+(in|cm|pt)\\\]//g' "$input_file"