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

TEMP_TEX="${input_file%.tex}-temp.tex" # Create a temp file name based on the input file
# Set the output file path
output_file="${base_name}.qmd"


# >>>>>>>>>>>>>>>>>>>>>>>> at LaTeX Level >>>>>>>>>>>>>>>>>>>>>>>>
echo "processing into temp latex"
# python3 $SCRIPT_DIR/process_eqref.py "$input_file" "$TEMP_TEX"
# pandoc "$TEMP_TEX" -s -o "$TEMP_TEX" -f latex -t latex
# echo "latex clean"


python3 $SCRIPT_DIR/process_marginnote.py "$TEMP_TEX" "$TEMP_TEX"
echo "margin done"
python3 $SCRIPT_DIR/process_figureref.py "$TEMP_TEX" "$TEMP_TEX"
echo "figure references done"
# <<<<<<<<<<<<<<<<<<<<<<<< at LaTeX Level <<<<<<<<<<<<<<<<<<<<<<<<


# Run Pandoc conversion
# pandoc "$TEMP_TEX" -o "$output_file" -f latex  -t markdown --filter $SCRIPT_DIR/filter.py
# echo "to qmd done"

# remove the [x in] or [x pt]
# sed -i '' -E 's/\\\[\-?\([0-9]*\)\(\.[0-9]+\)\?\(in\|cm\|pt\)\\\]//g' "$output_file"
# This script removes occurrences of LaTeX measurement units (e.g., \[10cm\], \[-5in\], etc.) from a file.

# The sed command is used to perform text substitution in a file.
# -i '' option is used to edit the file in-place without creating a backup.
# -E option enables extended regular expressions.
# 's/\\\[[-]?[0-9]*\.?[0-9]+(in|cm|pt)\\\]//g' is the regular expression pattern to match LaTeX measurement units.
# The pattern matches any number (positive or negative) followed by a unit (in, cm, or pt) enclosed in square brackets.
# The 'g' flag at the end of the pattern is used to perform the substitution globally (i.e., replace all occurrences).
# "$output_file" is the file path where the substitution will be performed.
sed -i '' -E 's/\\\[[-]?[0-9]*\.?[0-9]+(in|cm|pt)\\\]//g' "$output_file"
sed -i '' 's/\\\\linewidth//g' "$output_file"
sed -i '' 's/\[image\]/\[\]/g' "$output_file"
sed -i '' 's/\.pdf/.png/g' "$output_file"
sed -i '' 's/\.eps/\.png/g' "$output_file"
# sed -i '' -E 's/#fig:([^ ]+)/#fig-\1/g' "$output_file"
sed -i '' 's/height="\\\\textheight"//g' "$output_file"
sed -i '' 's/\\@fig-/@fig-/g' "$output_file"
sed -i '' 's/\\@eq/@eq/g' "$output_file"
sed -i '' 's/\\mathbbm/\\mathbb/g' "$output_file"
sed -i '' 's/sec:\(.*\)/sec-\1/g; s/chap:\(.*\)/sec-\1/g; s/chapter:\(.*\)/chapter-\1/g; s/eq:\(.*\)/eq-\1/g' "$output_file"
# sed -i '' -E 's/(:::\{\.column-margin\})(.*)(:::)/\1\n\2\n\3/g' "$output_file"


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

python3 $SCRIPT_DIR/shuffle_eqref.py "$output_file" "$output_file"
python3 $SCRIPT_DIR/process_marginnoteline.py "$output_file" "$output_file"
echo "Conversion completed: $output_file"