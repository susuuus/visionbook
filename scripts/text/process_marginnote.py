import re
import sys


def replace_margin_notes(text):
    """Replaces \margin{...} with :::{.column-margin}...::: while handling nested braces."""

    def replacer(match):
        inner_content = match.group(1)  # The content within \margin{...}
        return ":::\{.column-margin\}\n" + inner_content + ":::" + "\n"

    # pattern = r"\\marginnote\{((?:[^{}]+|\{(?:[^{}]+|\{[^{}]*\})*\})*)\}"
    pattern = r"\\marginnote\{([^{}]*)\}"
    return re.sub(pattern, replacer, text, flags=re.DOTALL)
