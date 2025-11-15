class MarkdownFormatter:
    def format(self, structured_content):
        text = "\n".join(structured_content.get("content", []))
        lines = text.splitlines()
        markdown_lines = []

        for line in lines:
            if line.strip():
                if len(line) > 50:
                    markdown_lines.append(f"## {line}")
                else:
                    markdown_lines.append(f"# {line}")
            else:
                markdown_lines.append("")

        return "\n".join(markdown_lines)


__all__ = ["MarkdownFormatter"]