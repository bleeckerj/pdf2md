try:
    from .parser import PDFParser
    from .formatters.markdown import MarkdownFormatter
except ImportError:  # pragma: no cover
    from parser import PDFParser
    from formatters.markdown import MarkdownFormatter


class PDFConverter:
    def __init__(self, pdf_parser=None, markdown_formatter=None):
        self.pdf_parser = pdf_parser or PDFParser()
        self.markdown_formatter = markdown_formatter or MarkdownFormatter()

    def convert(self, pdf_path):
        extracted_content = self.pdf_parser.extract(pdf_path)
        markdown_content = self.markdown_formatter.format(extracted_content)
        return markdown_content


__all__ = ["PDFConverter"]