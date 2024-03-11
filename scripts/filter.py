import panflute as pf
import re


def latex_to_markdown_cite(elem, doc):
    if isinstance(elem, pf.Cite):
        # Concatenate all citation keys with '@' prefix and separate them with commas (if multiple)
        citation_keys = ", ".join(f"@{citation.id}" for citation in elem.citations)

        # Create a new RawInline element with the concatenated citation keys
        # Ensure the format is set to 'markdown' to insert it as raw Markdown text
        return pf.RawInline(citation_keys, format="markdown")


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


def main(doc=None):
    return pf.run_filters(
        [latex_to_markdown_cite, convert_fig_ref, figure_refs],
        doc=doc,
    )


if __name__ == "__main__":
    main()
