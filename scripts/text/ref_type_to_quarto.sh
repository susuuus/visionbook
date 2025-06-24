#!/bin/bash

# Get the directory where the script is located
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the parent directory
parent_dir="$(dirname "$script_dir")"

# Get the grandparent directory (parent of the parent)
grandparent_dir="$(dirname "$parent_dir")"

# Set the directory to search for .qmd files
directory="$grandparent_dir"

# Loop over all .qmd files in the grandparent directory and its subdirectories
find "$directory" -name "*.qmd" | while read -r file; do
  # Make a backup of the original file
  original_file="$file.original"
  cp "$file" "$original_file"

  # Use perl to replace the phrase after "in" with the @reference, handling potential newlines after "in"
  perl -0777 -i -pe '
    s/
    \bin\b\s*               # Match the word "in" followed by any whitespace (including newlines)
    (.*?)                   # Non-greedy match of any characters (including newlines)
    \{reference-type="ref"  # Match the reference-type attribute
    \s*reference="([^"]+)"\}   # Match the reference attribute and capture "whatever"
    /in \@\2/gx             # Replace the whole phrase with "@whatever"
  ' "$file"

  # Check if the file has changed
  if ! cmp -s "$file" "$original_file"; then
    echo "Replaced references in: $file"
  fi

  # Remove the backup file
  rm "$original_file"
done

echo "Conversion completed for all .qmd files in $grandparent_dir."