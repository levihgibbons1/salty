"""Check required foundation files and simple local Markdown file links.

This is not a Markdown parser or an application/security test suite.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "CLAUDE.md", "GEMINI.md",
    "docs/architecture.md", "docs/milestone-1.md", "docs/access-tracker.md",
    "docs/decisions.md",
)
errors = []
for name in REQUIRED:
    path = ROOT / name
    if not path.is_file() or not path.read_text().strip():
        errors.append(f"Missing or empty required file: {name}")

files = list(ROOT.glob("*.md")) + list((ROOT / "docs").rglob("*.md"))
files += list((ROOT / ".github").rglob("*.md"))
for path in files:
    source = path.read_text()
    source = re.sub(r"```.*?```", "", source, flags=re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", source):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT) or not destination.exists():
            errors.append(f"{path.relative_to(ROOT)}: invalid local link {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Foundation checks passed ({len(files)} Markdown files).")
