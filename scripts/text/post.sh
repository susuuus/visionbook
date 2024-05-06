# post processing
# from qmd to qmd.
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
sed -i '' 's/\.pdf/.png/g' "$input_file"
sed -i '' 's/\.eps/\.png/g' "$input_file"
sed -i '' -E 's/#fig:([^ ]+)/#fig-\1/g' "$input_file"
sed -i '' 's/\\\\linewidth//g' "$input_file" 
# sed -i '' -E 's/(width=".*?)(\\\\linewidth")/\1"/g' "$input_file"
sed -i '' 's/sec:\(.*\)/sec-\1/g; s/chap:\(.*\)/chap-\1/g; s/chapter:\(.*\)/chapter-\1/g; s/eq:\(.*\)/eq-\1/g' "$input_file"

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
    -e 's/\\lightfield/L/g' "$input_file"
