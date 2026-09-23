import os
import markdown
from os import walk

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog Post</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <div class="app-shell">
        <main class="container">
            <article class="markdown-body">
                {content}
            </article>
        </main>
    </div>
</body>
</html>"""


def convert_files(path: str) -> None:
    with open(path, "r") as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text, extensions=["fenced_code", "tables"])

    with open(path.replace("md", "html"), "w") as f:
        f.write(TEMPLATE.format(content=html_content))


def main() -> None:
    for dirpath, _, filenames in walk("."):
        for f in filenames:
            if f.endswith(".md"):
                concat_path = os.path.join(dirpath, f)
                convert_files(concat_path)


if __name__ == "__main__":
    main()
