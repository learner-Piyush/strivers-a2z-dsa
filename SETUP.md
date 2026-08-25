# Setup

## 1. Python environment

You don't strictly *need* a venv to solve standalone DSA problems (no dependencies
beyond the standard library for most of them), but it's good practice and needed
if you want `pytest`/`black`/`flake8` isolated from your other projects.

```bash
python3 -m venv venv

# activate it
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows (cmd/PowerShell)

pip install -r requirements.txt
```

Reactivate the venv (`source venv/bin/activate`) each time you open a new
terminal to work on this repo. `venv/` is already git-ignored.

## 2. Enable the commit hook (asks for difficulty)

Git doesn't use `.githooks/` by default — point it there once per clone:

```bash
git config core.hooksPath .githooks
```

Now, whenever you `git add` a new file under `solutions/` and run
`git commit`, it will interactively ask for difficulty, title, topic, and
source URL, and stamp them into the file's header automatically — this is
what `scripts/update_readme.py` reads to update the counters.

If a file already has a `Difficulty:` header (e.g. you wrote it yourself),
the hook skips it and leaves it alone.

## 3. GitHub repo settings

- **Settings → Actions → General → Workflow permissions** → set to
  **"Read and write permissions"**. Without this, `update-readme-on-push.yml`
  can't push the updated README back.
- **Settings → Secrets and variables → Actions → New repository secret**
  → name it `DISCORD_WEBHOOK_URL`, value = your Discord channel's webhook URL
  (Discord: Channel Settings → Integrations → Webhooks → New Webhook → Copy URL).

## 4. Daily workflow

1. Solve a problem, save it under the matching `solutions/<topic>/` folder.
2. `git add solutions/<topic>/your_file.py`
3. `git commit -m "solved: <problem name>"` → hook asks difficulty, stamps header.
4. `git push` → the update-readme workflow recounts and commits the new README counters.
5. If you haven't pushed anything by the next hour check (Mon–Sat), you'll get pinged on Discord.
