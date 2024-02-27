import panflute as pf


def latex_to_markdown_cite(elem, doc):
    if isinstance(elem, pf.Cite):
        # Concatenate all citation keys with '@' prefix and separate them with commas (if multiple)
        citation_keys = ", ".join(f"@{citation.id}" for citation in elem.citations)

        # Create a new RawInline element with the concatenated citation keys
        # Ensure the format is set to 'markdown' to insert it as raw Markdown text
        return pf.RawInline(citation_keys, format="markdown")


def main(doc=None):
    return pf.run_filter(latex_to_markdown_cite, doc=doc)


if __name__ == "__main__":
    main()
