"""Generate one interview page per topic. Not part of the published site."""

import html
from pathlib import Path

TOPICS = [
    ("aks", "AKS"),
    ("eks", "EKS"),
    ("terraform", "Terraform"),
    ("docker", "Docker"),
    ("kubernetes", "Kubernetes"),
    ("devops", "DevOps"),
    ("git", "Git"),
    ("cloudops", "CloudOps"),
]

NAV = """
        <h1><a href="../index.html">Soma Mahapatra</a></h1>
        <p>Interview questions with answers, beginner through advanced.</p>
        <h2>Interview</h2>
        <ul>
            <li><a href="aks.html"{aks}>AKS</a></li>
            <li><a href="eks.html"{eks}>EKS</a></li>
            <li><a href="terraform.html"{terraform}>Terraform</a></li>
            <li><a href="docker.html"{docker}>Docker</a></li>
            <li><a href="kubernetes.html"{kubernetes}>Kubernetes</a></li>
            <li><a href="devops.html"{devops}>DevOps</a></li>
            <li><a href="git.html"{git}>Git</a></li>
            <li><a href="cloudops.html"{cloudops}>CloudOps</a></li>
            <li><a href="security.html">Security scans</a></li>
            <li><a href="../with-ai.html">Built with AI</a></li>
        </ul>
        <h2>Back</h2>
        <ul>
            <li><a href="../index.html">Home</a></li>
        </ul>
"""

STYLE = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; background: #fafbfc; }
        .container { display: flex; min-height: 100vh; }
        aside { width: 250px; background: #fff; border-right: 1px solid #e1e4e8; padding: 2rem 1.5rem; position: fixed; height: 100vh; overflow-y: auto; }
        aside h1 { font-size: 1.1rem; margin-bottom: 0.5rem; }
        aside h1 a { color: #24292e; text-decoration: none; }
        aside p { font-size: 0.85rem; color: #666; margin-bottom: 1rem; }
        aside h2 { font-size: 0.75rem; text-transform: uppercase; color: #999; margin: 1.5rem 0 0.75rem; }
        aside ul { list-style: none; }
        aside a { text-decoration: none; color: #0366d6; font-size: 0.9rem; display: block; padding: 0.25rem 0; }
        aside a.active { color: #6f42c1; font-weight: 600; border-left: 2px solid #6f42c1; padding-left: 8px; }
        main { margin-left: 250px; padding: 3rem; flex: 1; max-width: 920px; }
        h1 { margin-bottom: 1rem; font-size: 2rem; border-bottom: 2px solid #e1e4e8; padding-bottom: 0.5rem; }
        h2 { margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.4rem; }
        .qa { background: #fff; border: 1px solid #e1e4e8; border-radius: 6px; padding: 1rem 1.25rem; margin: 0.75rem 0; }
        .qa h3 { font-size: 1rem; margin-bottom: 0.5rem; }
        .qa p { color: #444; }
        code { background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
"""


def page(slug, title, items):
    if len(items) != 100:
        raise SystemExit(f"{slug} has {len(items)} questions, expected 100")
    flags = {name: "" for name, _ in TOPICS}
    flags[slug] = ' class="active"'
    nav = NAV.format(**flags)
    bands = [("Beginner", items[:34]), ("Intermediate", items[34:67]), ("Advanced", items[67:])]
    body = []
    number = 1
    for band, rows in bands:
        body.append(f"<h2>{band}</h2>")
        for question, answer in rows:
            body.append(
                "<article class=\"qa\">"
                f"<h3>{number}. {html.escape(question)}</h3>"
                f"<p>{html.escape(answer)}</p>"
                "</article>"
            )
            number += 1
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} interview questions</title>
    <style>{STYLE}</style>
</head>
<body>
<div class="container">
    <aside>{nav}</aside>
    <main>
        <h1>{html.escape(title)}: 100 interview questions</h1>
        <p>Thirty-four beginner questions, thirty-three intermediate, and thirty-three advanced. Each one has a direct answer.</p>
        {''.join(body)}
    </main>
</div>
</body>
</html>
"""


def main():
    root = Path(__file__).resolve().parent
    for slug, title in TOPICS:
        namespace = {}
        exec((root / "_src" / f"{slug}.py").read_text(encoding="utf-8"), namespace)
        items = namespace["QUESTIONS"]
        if len(items) > 100:
            items = items[:67] + items[-33:]
        html_text = page(slug, title, items)
        (root / f"{slug}.html").write_text(html_text, encoding="utf-8")
        print(slug, len(namespace["QUESTIONS"]))


if __name__ == "__main__":
    main()
