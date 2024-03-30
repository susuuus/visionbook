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

TEMP_TEX="${input_file%.tex}-temp.tex" # Create a temp file name based on the input file

python3 $SCRIPT_DIR/process_eqref.py "$input_file" "$TEMP_TEX"
echo "eq references done"

# pandoc "$TEMP_TEX" -s -o "$TEMP_TEX" -f latex -t latex
# echo "latex clean"

python3 $SCRIPT_DIR/process_marginnote.py "$TEMP_TEX" "$TEMP_TEX"
echo "margin done"
python3 $SCRIPT_DIR/process_figureref.py "$TEMP_TEX" "$TEMP_TEX"
echo "figure references done"
# Run Pandoc conversion
pandoc "$TEMP_TEX" -o "$output_file" -f latex  -t markdown --filter $SCRIPT_DIR/filter.py
echo "to qmd done"

# remove the [x in] or [x pt]
# sed -i '' -E 's/\\\[\-?\([0-9]*\)\(\.[0-9]+\)\?\(in\|cm\|pt\)\\\]//g' "$output_file"
sed -i '' -E 's/\\\[[-]?[0-9]*\.?[0-9]+(in|cm|pt)\\\]//g' "$output_file"
sed -i '' 's/\.pdf/.png/g' "$output_file"
sed -i '' 's/\.eps/\-1.png/g' "$output_file"
sed -i '' -E 's/#fig:([^ ]+)/#fig-\1/g' "$output_file"
sed -i '' 's/\\\\linewidth//g' "$output_file"
sed -i '' -E 's/#fig:([^ ]+)/#fig-\1/g' "$output_file"
sed -i '' 's/\\@fig-/@fig-/g' "$output_file"
sed -i '' 's/\\@eq/@eq/g' "$output_file"
sed -i '' 's/sec:\(.*\)/sec-\1/g; s/chap:\(.*\)/chap-\1/g; s/chapter:\(.*\)/chapter-\1/g; s/eq:\(.*\)/eq-\1/g' "$output_file"
sed -i '' 's/\[image\]/\[\]/g' "$output_file"
sed -i '' 's/height="\\\\textheight"//g' "$output_file"
sed -i '' -E 's/(:::\{\.column-margin\})(.*)(:::)/\1\n\2\n\3/g' "$output_file"


sed -i '' -e 's/\\img/\\ell/g' \
    -e 's/\\imgin/\\ell\\_{\\texttt{in}}/g' \
    -e 's/\\imgout/\\ell_{\\texttt{out}}/g' \
    -e 's/\\boldimg/\\boldsymbol\\ell/g' \
    -e 's/\\boldimgin/\\boldsymbol\\ell_{\\texttt{in}}/g' \
    -e 's/\\boldimgout/\\boldsymbol\\ell_{\\texttt{out}}/g' \
    -e 's/\\capitalimg/\\mathscr{L}/g' \
    -e 's/\\boldcapitalimg/\\mathscr{L}/g' \
    -e 's/\\capitalimgin/\\mathscr{L}_{\\texttt{in}}/g' \
    -e 's/\\capitalimgout/\\mathscr{L}_{\\texttt{out}}/g' \
    -e 's/\\lightfield/L/g' "$output_file"

python3 $SCRIPT_DIR/process_marginnoteline.py "$output_file" "$output_file"
python3 $SCRIPT_DIR/shuffle_eqref.py "$output_file" "$output_file"
echo "Conversion completed: $output_file"