class PDFToMarkdownConverter:
    def __init__(self, pdf_parser, markdown_formatter):
        self.pdf_parser = pdf_parser
        self.markdown_formatter = markdown_formatter

    def convert(self, pdf_path):
        extracted_content = self.pdf_parser.extract(pdf_path)
        markdown_content = self.markdown_formatter.format(extracted_content)
        return markdown_content

def main():
    # This function will be implemented in the cli.py file to handle command-line arguments
    pass

if __name__ == "__main__":
    main()