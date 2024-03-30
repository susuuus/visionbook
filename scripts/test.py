import re

text = "derivatives in equations (\\ref{eq:image_partial_derivatives_aprox}). Using this approximation, \\eqn{\\ref{eqn:derivative_Y_along_edge}} can be written as follows:"

# Regular expression pattern to find all occurrences of \ref{...} and \eqn{\ref{...}}
pattern = r"\\ref{eq:([^}]*)}|\\eqn{\\ref{eqn:([^}]*)}}"


# Replacement function to format matches
def replacement(match):
    label = match.group(1) if match.group(1) else match.group(2)
    return f"@eq-{label}"


# Performing the replacement
simplified_text = re.sub(pattern, replacement, text)

print(simplified_text)
