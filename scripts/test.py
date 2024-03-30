import re

# Example text that includes patterns to be rearranged
text = """$$\\begin{aligned}
\\frac{\\partial \\ell}{\\partial x} & \\simeq & \\ell(x,y) - \\ell(x-1,y) \\
\\frac{\\partial \\ell}{\\partial y} & \\simeq & \\ell(x,y) - \\ell(x,y-1) 
#eq-image_partial_derivatives_aprox
\\end{aligned}$$"""

# Updated regular expression to match the pattern across multiple lines and capture the necessary parts
pattern = r"(\$\$.*?)(#eq-[\w-]+)(.*?)\$\$"

# Function to rearrange the matched pattern
replacement = r"\1\3\2"

# Replace all occurrences in the text using re.DOTALL to match across newlines
rearranged_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

print(rearranged_text)
