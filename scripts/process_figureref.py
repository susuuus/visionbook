import re
import sys


def convert_fig_refs(input_file_path, output_file_path):
    # Read the content of the LaTeX file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Define the regular expression pattern for the substitution
    # This pattern captures the 'whatever' part of the fig reference
    pattern = r"\\Fig\{\\ref\{fig:(.*?)\}\}"

    # Replace the pattern in the content
    # The replacement pattern uses the captured group from the match
    modified_content = re.sub(pattern, r"@fig-\1", content)

    # Write the modified content to the output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    convert_fig_refs(input_file_path, output_file_path)
