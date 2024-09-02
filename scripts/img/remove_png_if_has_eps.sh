#!/bin/bash

# Directory to search for files
directory="/Users/shenshen/code/cv_book/figures"

# Loop through all .eps files in the directory and its subdirectories
find "$directory" -type f -name "*.eps" | while read eps_file; do
    # Get the directory and base name without the extension
    dir_name=$(dirname "$eps_file")
    base_name=$(basename "$eps_file" .eps)
    
    # Construct the corresponding .png file name
    png_file="$dir_name/$base_name.png"
    
    # Check if the .png file exists
    if [ -f "$png_file" ]; then
        # Delete the .png file
        rm "$png_file"
        echo "Deleted $png_file"
    fi
done