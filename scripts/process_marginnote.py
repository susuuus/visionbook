import re
import sys


def replace_margin_notes(text):
    """Replaces \margin{...} with :::{.column-margin}...::: while handling nested braces."""

    def replacer(match):
        inner_content = match.group(1)  # The content within \margin{...}
        return ":::\{.column-margin\}" + inner_content + ":::"

    pattern = r"\\marginnote\{((?:[^{}]+|\{(?:[^{}]+|\{[^{}]*\})*\})*)\}"
    return re.sub(pattern, replacer, text)


def process_latex_file(input_file_path, output_file_path):
    """Reads LaTeX from input file, replaces \margin{...} commands, and writes to output file."""
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    modified_content = replace_margin_notes(content)

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    process_latex_file(input_file_path, output_file_path)
