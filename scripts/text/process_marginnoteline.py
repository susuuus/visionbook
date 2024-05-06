import re
import sys


def add_line_breaks(input_file_path, output_file_path):
    # Read the content of the file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Define the regular expression pattern for the substitution
    pattern = r"(:::\{\.column-margin\})(.*?)(:::)"

    # Replace the pattern in the content, adding line breaks as specified
    modified_content = re.sub(pattern, r"\n\n\1\n\2\n\3\n\n", content, flags=re.DOTALL)

    # Write the modified content to the output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    add_line_breaks(input_file_path, output_file_path)
