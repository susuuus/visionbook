import re
import sys

import os


def current_script_path():
    script_path = os.path.realpath(__file__)
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    return parent_directory


def convert_eq_refs(input_file_path, output_file_path):
    # Read the content of the LaTeX file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()
    modified_content = re.sub(r"\\ref\{eq:(.*?)\}", r"@eq-\1", content)
    modified_content = re.sub(
        r"\\eqn\{\\ref\{eqn:(.*?)\}\}", r"@eq-\1", modified_content
    )
    modified_content = re.sub(r"\\label\{eq:(.*?)\}", r"#eq-\1", modified_content)
    modified_content = re.sub(r"\\label\{eqn:(.*?)\}", r"#eq-\1", modified_content)
    modified_content = re.sub(r"\\eqref\{eq:(.*?)\}", r"@eq-\1", modified_content)
    modified_content = re.sub(r"\\centerline", "", modified_content)
    modified_content = re.sub(r"^\s*%.*$\n?", "", modified_content, flags=re.MULTILINE)

    pattern = r"\\ref{eq:([^}]*)}|\\eqn{\\ref{eqn:([^}]*)}}"

    # Replacement function to format matches
    def replacement(match):
        label = match.group(1) if match.group(1) else match.group(2)
        return f"@eq-{label}"

    # Performing the replacement
    modified_content = re.sub(pattern, replacement, modified_content)
    # Write the modified content to the output file
    path = current_script_path() + "../src/setup.tex"
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write("\include{" + path + "}")
        file.write("\n")
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    convert_eq_refs(input_file_path, output_file_path)
