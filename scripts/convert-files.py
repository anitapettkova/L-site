import os
from os import walk
import markdown

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dev Log</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>

    <div class="app-shell">
        <header class="site-header">
            <a href="/" class="brand">
                <span>DEV_LOG</span>
                <span class="brand-badge">v2.0</span>
            </a>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about/">About</a></li>
                    <li><a href="/blog/">Blog</a></li>
                </ul>
            </nav>
        </header>

        <main class="container">
            <article class="markdown-body">
                {content}
            </article>
        </main>

        <footer>
            <div>STATUS: Operational</div>
            <div id="sys-time">SYS_TIME: --:--:--</div>
        </footer>
    </div>

    <!-- Essential JS Script for dynamic navigation and clock -->
    <script src="/assets/js/main.js"></script>
</body>
</html>"""


def extract_title(md_text: str, fallback_filename: str) -> str:
    """Extracts the first H1 header (# Title) or falls back to filename."""
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line.replace("# ", "").strip()

    base = os.path.basename(fallback_filename)
    clean_name = os.path.splitext(base)[0].replace("-", " ").replace("_", " ")
    return clean_name.title()


def convert_files(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        md_text = f.read()

    page_title = extract_title(md_text, path)

    html_content = markdown.markdown(
        md_text, extensions=["fenced_code", "tables", "nl2br"]
    )

    final_html = TEMPLATE.format(title=page_title, content=html_content)

    output_path = os.path.splitext(path)[0] + ".html"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Generated: {output_path}")


def main() -> None:
    for dirpath, _, filenames in walk("."):
        for f in filenames:
            if f.endswith(".md"):
                concat_path = os.path.join(dirpath, f)
                convert_files(concat_path)


if __name__ == "__main__":
    main()
