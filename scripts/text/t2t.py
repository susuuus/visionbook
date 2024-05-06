# latex to latex plain text replacement.

import re, sys


def process_latex_file(input_file_path, output_file_path, commands=None):
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    for i in commands:
        content = globals()[i](content)

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(content)


def colon_to_hyphen(latex_content):
    # all colon inside \label and \ref becomes hyphen.

    # \label{fig:gradient_descent:optimization_schematic} or \ref{fig:gradient _descent:optimization_schematic} becomes ?{fig-gradient _descent-optimization_schematic}

    # This pattern captures contents within \label or \ref followed by {key}
    # This regex pattern targets \label{...} or \ref{...}
    pattern = r"(\\label|\\ref)\{([^}]+)\}"

    # Function to replace ':' with '-' in the captured group
    def replace_colon(match):
        command = match.group(1)  # \label or \ref
        key = match.group(2).replace(
            ":", "-"
        )  # Replace colons with hyphens in the label/ref key
        return f"{command}{{{key}}}"  # Recreate the full label/ref command with modified key

    # Replace using the pattern and function
    return re.sub(pattern, replace_colon, latex_content)


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    commands = sys.argv[3:]
    process_latex_file(input_file_path, output_file_path, commands=commands)
