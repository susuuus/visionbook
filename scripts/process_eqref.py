import re
import sys


def convert_eq_refs(input_file_path, output_file_path):
    # Read the content of the LaTeX file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    modified_content = re.sub(r"\\label\{eq:(.*?)\}", r"#eq-\1", content)
    modified_content = re.sub(r"\\eqref\{eq:(.*?)\}", r"@eq-\1", modified_content)
    modified_content = re.sub(r"\\eqn\\ref\{eq:(.*?)\}", r"@eq-\1", modified_content)
    modified_content = re.sub(
        r"\\eqn\{\\ref\{eqn:(.*?)\}\}", r"@eq-\1", modified_content
    )
    modified_content = re.sub(r"\\ref\{eq:(.*?)\}", r"@eq-\1", modified_content)
    # Write the modified content to the output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)


# Example usage:
if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    convert_eq_refs(input_file_path, output_file_path)
