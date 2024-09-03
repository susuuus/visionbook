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

  # Replace fig-something:something, eq-something:something, and sec-something:something with hyphen instead of colon
  perl -0777 -i -pe 's/(fig|eq|sec)-([^\s:]+):([^\s]+)/\1-\2-\3/g' "$file"

  # Check if the file has changed
  if ! cmp -s "$file" "$original_file"; then
    echo "Replaced colons with hyphens in: $file"
  fi

  # Remove the backup file
  rm "$original_file"
done

echo "Colon to hyphen conversion completed for all .qmd files in $grandparent_dir."