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
        # Replace matched patterns
        text = re.sub(pattern, r"@fig-\1", elem.text)
        # If a replacement occurred, return a new RawInline element with the updated text
        if text != elem.text:
            return pf.RawInline(text, format="markdown")


def convert_marginnote(elem, doc):
    if isinstance(elem, pf.RawInline) and "\marginnote{" in elem.text:
        # Extract the content within the LaTeX command
        content = elem.text.split("\marginnote{", 1)[1].rstrip("}")
        # Create a new Div element with the extracted content, wrapped in a Paragraph
        new_elem = pf.Div(pf.Para(pf.Str(content)), classes=["column-margin"])
        return new_elem


def main(doc=None):
    return pf.run_filters(
        [latex_to_markdown_cite, convert_fig_ref, convert_marginnote], doc=doc
    )


if __name__ == "__main__":
    main()
