import re
import sys


def convert_eq_refs(input_file_path, output_file_path):
    # Read the content of the LaTeX file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Updated regular expression to match the pattern across multiple lines and capture the necessary parts
    pattern = r"(\$\$.*?)(#eq-[\w-]+)(.*?\$\$)"

    # Function to rearrange the matched pattern
    replacement = r"\1\3{\2}"

    # Replace all occurrences in the text using re.DOTALL to match across newlines
    modified_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write the modified content to the output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    convert_eq_refs(input_file_path, output_file_path)
