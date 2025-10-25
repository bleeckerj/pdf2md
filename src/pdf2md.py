#!/usr/bin/env python3
import sys
import argparse
from converter import PDFConverter

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to Markdown format.")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Output Markdown file (default: stdout)")
    args = parser.parse_args()

    converter = PDFConverter()
    markdown_text = converter.convert(args.pdf)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(markdown_text)
    else:
        print(markdown_text)

if __name__ == "__main__":
    main()