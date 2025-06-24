import panflute as pf
import re


def latex_to_markdown_cite(elem, doc):
    if isinstance(elem, pf.Cite):
        # Concatenate all citation keys with '@' prefix and separate them with commas (if multiple)
        citation_keys = ", ".join(f"@{citation.id}" for citation in elem.citations)

        # Create a new RawInline element with the concatenated citation keys
        # Ensure the format is set to 'markdown' to insert it as raw Markdown text
        return pf.RawInline(citation_keys, format="markdown")


def latex_to_markdown_label(elem, doc):
    if isinstance(elem, pf.RawBlock) and elem.format == "latex":
        # Check if the block is a LaTeX raw block
        latex_content = elem.text.strip()
        if latex_content.startswith("\\label{"):
            # Extract the label content between { and }
            label_content = latex_content[len("\\label{") : -1]
            # Customize the conversion based on the label content
            # For example, you can perform different actions based on label_content
            # Here, we just return a markdown comment with the label content
            label_content = label_content.replace(":", "-")
            markdown_content = "#" + label_content
            return pf.RawBlock(markdown_content, format="markdown")


def latex_to_markdown_ref(elem, doc):
    if isinstance(elem, pf.RawBlock) and elem.format == "latex":
        # Check if the block is a LaTeX raw block
        latex_content = elem.text.strip()
        if latex_content.startswith("\\ref"):
            # Extract the label content between { and }
            label_content = latex_content[len("\\ref{") : -1]
            # Customize the conversion based on the label content
            # For example, you can perform different actions based on label_content
            # Here, we just return a markdown comment with the label content
            label_content = label_content.replace(":", "-")
            markdown_content = "#" + label_content
            return pf.RawBlock(markdown_content, format="markdown")


def convert_fig_ref(elem, doc):
    if isinstance(elem, pf.RawInline) and elem.format == "tex":
        # Pattern to match \Fig.\ref{fig:whatever} and capture 'whatever'
        pattern = r"\\Fig\\.ref\{fig:(.*?)\}"
        pattern = r"\\fig\\.ref\{fig:(.*?)\}"
        # Replace matched patterns
        text = re.sub(pattern, r"@fig-\1", elem.text)
        # If a replacement occurred, return a new RawInline element with the updated text
        if text != elem.text:
            return pf.RawInline(text, format="markdown")


def convert_marginnote(elem, doc):
    if isinstance(elem, pf.RawInline):
        pattern = r"\{(.*?)\}"
        replacement = r"::: {.column-margin}\1:::"
        new_text = re.sub(pattern, replacement, elem.text)
        return pf.RawInline(new_text, format="markdown")


def figure_refs(elem, doc):
    if isinstance(elem, pf.RawInline) and elem.format == "latex":
        # Check if the LaTeX command is \ref{fig:something}
        if elem.text.startswith("\\ref{fig:"):
            fig_id = elem.text[5:-1]  # Extract 'fig:something'
            return pf.Str(f"@{fig_id}")  # Replace with '@fig-something'

        # Check if the LaTeX command is \label{fig:something}
        elif elem.text.startswith("\\label{fig:"):
            fig_id = elem.text[7:-1]  # Extract 'fig:something'
            return pf.RawInline(
                f"{{#{fig_id}}}", format="markdown"
            )  # Replace with '{#fig-something}'


def replace_norm(elem, doc):
    if (
        type(elem) == pf.Math
        or isinstance(elem, pf.RawInline)
        or isinstance(elem, pf.RawBlock)
    ):
        # Use regex to find and replace the \norm{...} pattern
        new_text = re.sub(
            r"\\norm\{(.*?)\}",
            lambda match: "\\{\\left\\lVert{" + match.group(1) + "}\\right\\rVert\\}",
            elem.text,
        )
        elem.text = new_text


def replace_simple(elem, doc):
    if type(elem) == pf.Math:
        elem.text = elem.text.replace("\\given", "\\bigm |")
        elem.text = elem.text.replace("\\transpose", "\\mathsf{T}")


def main(doc=None):
    return pf.run_filters(
        [
            latex_to_markdown_cite,
            latex_to_markdown_label,
            latex_to_markdown_ref,
            # replace_norm,
            # replace_simple,
        ],
        doc=doc,
    )


if __name__ == "__main__":
    main()
