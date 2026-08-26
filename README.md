# Striver's A2Z DSA Sheet — Python Solutions

Daily DSA practice (Mon–Sat) following the [Striver A2Z Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z), solved in Python.

## Progress

| Difficulty | Solved |
|---|---|
| 🟢 Easy | <!--EASY_START-->6 / 152<!--EASY_END--> |
| 🟡 Medium | <!--MEDIUM_START-->0 / 186<!--MEDIUM_END--> |
| 🔴 Hard | <!--HARD_START-->0 / 136<!--HARD_END--> |
| **Total** | <!--TOTAL_START-->6 / 474<!--TOTAL_END--> |

*Counters update automatically on every push — see `scripts/update_readme.py`. If the sheet grows, edit the denominators in this table (search for `EASY_TOTAL` etc. in `scripts/update_readme.py`) and they'll stay in sync.*

## Structure

Nest folders as deep as the sheet needs — e.g.:

```
solutions/
  01_Learn_the_basics/
    01_Things_to_know_in_Python/
      input_output.py
  ...
```

Scaffold a new one instead of `mkdir -p`ing by hand:

```bash
python scripts/new_problem.py "01_Learn_the_basics/01_Things_to_know_in_Python" "Input Output"
```

This creates `solutions/01_Learn_the_basics/01_Things_to_know_in_Python/input_output.py` (folders auto-created) with a bare stub — no header. Write your solution, then `git add` + `git commit` as usual; the pre-commit hook (see `SETUP.md`) asks for difficulty/title/topic/source and stamps the header in for you, at any depth. You never type the header by hand.

## Daily reminder

A GitHub Action checks hourly (Mon–Sat) whether a solution file has been pushed today. If not, it pings a Discord webhook every hour until one lands. See `.github/workflows/daily-reminder.yml`.

## Setup

See `SETUP.md` for local environment setup (venv), and enabling the commit hook that asks for problem difficulty.
