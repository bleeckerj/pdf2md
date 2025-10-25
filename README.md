# 📄➡️📝 pdf2md - PDF to Markdown Converter

pdf2md is a Python project that converts PDF documents into structured Markdown format. This tool is designed to provide a more organized output than plain text, making it easier to work with the content of PDF files in various applications.

*Built with ❤️ by [Near Future Laboratory](https://nearfuturelaboratory.com)*

## ✨ Features

- 📄 Converts PDF files to Markdown format
- 🏗️ Retains the structure of the original document, including headings, lists, and links
- 🖥️ Easy to use command-line interface
- 🚀 Fast and efficient conversion process

## 🚀 Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## 🎯 Usage

To convert a PDF file to Markdown, use the command line interface:

```
python -m src.pdf2md <path_to_pdf_file> -o <output_markdown_file>
```

Replace `<path_to_pdf_file>` with the path to your PDF file and `<output_markdown_file>` with the desired output Markdown file name.

## 📁 Project Structure

```
pdf2md
├── src
│   ├── __init__.py
│   ├── pdf2md.py
│   ├── converter.py
│   ├── parser.py
│   └── formatters
│       ├── __init__.py
│       ├── markdown.py
│       └── base.py
├── tests
│   ├── __init__.py
│   ├── test_converter.py
│   ├── test_parser.py
│   └── test_formatters.py
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes. 

We'd love to hear from you! 💬

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

*Made with 🔬 innovation at [Near Future Laboratory](https://nearfuturelaboratory.com)*