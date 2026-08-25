"""
Creates a new, empty solution file at any depth under solutions/, making
parent folders as needed. You do NOT write the metadata header here — the
pre-commit hook fills that in automatically when you commit (see
.githooks/pre-commit). This script just saves you `mkdir -p`.

Usage:
    python scripts/new_problem.py "01_Learn_the_basics/01_Things_to_know_in_Python" "Input Output"

This creates:
    solutions/01_Learn_the_basics/01_Things_to_know_in_Python/input_output.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = REPO_ROOT / "solutions"

STUB = '''# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


def solve():
    pass


if __name__ == "__main__":
    solve()
'''


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def main():
    if len(sys.argv) != 3:
        print('Usage: python scripts/new_problem.py "<folder/path>" "<Problem Name>"')
        sys.exit(1)

    folder_path, problem_name = sys.argv[1], sys.argv[2]
    target_dir = SOLUTIONS_DIR / folder_path
    target_dir.mkdir(parents=True, exist_ok=True)

    filename = slugify(problem_name) + ".py"
    target_file = target_dir / filename

    if target_file.exists():
        print(f"Already exists: {target_file.relative_to(REPO_ROOT)}")
        sys.exit(1)

    target_file.write_text(STUB, encoding="utf-8")
    print(f"Created: {target_file.relative_to(REPO_ROOT)}")
    print("Write your solution, then `git add` + `git commit` it as usual.")


if __name__ == "__main__":
    main()
