"""
Scans solutions/ for .py files with a `Difficulty:` header, counts them,
and rewrites the counter table in README.md between the HTML comment markers.

Run manually:   python scripts/update_readme.py
Run in CI:       used by .github/workflows/update-readme-on-push.yml
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = REPO_ROOT / "solutions"
README_PATH = REPO_ROOT / "README.md"

# Update these if the sheet's question count changes.
EASY_TOTAL = 152
MEDIUM_TOTAL = 186
HARD_TOTAL = 136

DIFFICULTY_RE = re.compile(r"Difficulty:\s*(Easy|Medium|Hard)", re.IGNORECASE)


def count_solutions() -> dict:
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    if not SOLUTIONS_DIR.exists():
        return counts

    for py_file in SOLUTIONS_DIR.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8", errors="ignore")
        match = DIFFICULTY_RE.search(text)
        if match:
            difficulty = match.group(1).capitalize()
            counts[difficulty] += 1
        else:
            print(f"WARNING: no Difficulty header found in {py_file}")

    return counts


def replace_between(content: str, marker: str, new_value: str) -> str:
    pattern = re.compile(
        rf"(<!--{marker}_START-->)(.*?)(<!--{marker}_END-->)", re.DOTALL
    )
    if not pattern.search(content):
        raise ValueError(f"Marker {marker} not found in README.md")
    return pattern.sub(rf"\g<1>{new_value}\g<3>", content)


def main():
    counts = count_solutions()
    total_solved = sum(counts.values())
    total_all = EASY_TOTAL + MEDIUM_TOTAL + HARD_TOTAL

    readme = README_PATH.read_text(encoding="utf-8")
    readme = replace_between(readme, "EASY", f"{counts['Easy']} / {EASY_TOTAL}")
    readme = replace_between(readme, "MEDIUM", f"{counts['Medium']} / {MEDIUM_TOTAL}")
    readme = replace_between(readme, "HARD", f"{counts['Hard']} / {HARD_TOTAL}")
    readme = replace_between(readme, "TOTAL", f"{total_solved} / {total_all}")
    README_PATH.write_text(readme, encoding="utf-8")

    print(f"Easy: {counts['Easy']}/{EASY_TOTAL}")
    print(f"Medium: {counts['Medium']}/{MEDIUM_TOTAL}")
    print(f"Hard: {counts['Hard']}/{HARD_TOTAL}")
    print(f"Total: {total_solved}/{total_all}")


if __name__ == "__main__":
    main()
