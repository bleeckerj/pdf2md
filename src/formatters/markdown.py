def format_text_to_markdown(text):
    # Convert plain text to Markdown format
    # This is a simple implementation; more complex formatting can be added as needed
    lines = text.splitlines()
    markdown_lines = []

    for line in lines:
        if line.strip():  # Non-empty line
            # Example: Convert headings based on line length or content
            if len(line) > 50:
                markdown_lines.append(f"## {line}")  # Subheading for long lines
            else:
                markdown_lines.append(f"# {line}")  # Main heading for shorter lines
        else:
            markdown_lines.append("")  # Preserve empty lines

    return "\n".join(markdown_lines)


def format_list_to_markdown(items):
    # Convert a list of items to Markdown list format
    return "\n".join(f"- {item}" for item in items)


def format_table_to_markdown(table):
    # Convert a 2D list (table) to Markdown table format
    markdown_table = []
    for row in table:
        markdown_table.append("| " + " | ".join(row) + " |")
    return "\n".join(markdown_table)