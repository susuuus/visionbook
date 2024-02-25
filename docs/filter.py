import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Image):
        # This block ensures that Image elements are handled correctly.
        # Pandoc automatically converts image references to <img> tags in HTML.
        pass  # You can add additional transformations here if needed.


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
