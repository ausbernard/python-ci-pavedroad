## ✅ Recommended Layout
```
python-cicd-template/
├─ "(app-name)"
│  └─ src
│    └─ __init__.py
|    └─ app.py
├─ tests/
│  └─ test_health.py
├─ pyproject.toml
├─ requirements.txt        # exported from pyproject for Docker
├─ .pre-commit-config.yaml
└─ README.md
```

## 📦 Create a pyproject.toml (one file to rule them all)
```ini
[project]
name = ""
version = ""
description = ""
readme = ""
requires-python = ""
license = {text = ""}
authors = [{ name = "" }]
# keep small
dependencies = [
  "",
  "",
]

[project.optional-dependencies]
dev = [
  "pytest",
  "pytest-cov",
  "black",
  "ruff",
  "pre-commit",
  "httpx",  # needed for fastapi.testclient module
  # optional but nice:
  "mypy",
  "types-requests",
]

[tool.black]
line-length = 100
target-version = ["py311"]
exclude = '/(\.venv|build|dist|.history)/'  # exclude must be a string

[tool.ruff]
line-length = 100
target-version = "py311"
# Pick a sane set; you can expand later
select = ["E", "F", "W", "I"]  # pycodestyle, pyflakes, warnings, isort
ignore = ["E501"]              # black handles line length
exclude = [".venv", "build", "dist", ".history"]


[tool.ruff.format]
quote-style = "double"

[tool.pytest.ini_options]

# Optional strict typing (if you use mypy)
[tool.mypy]
```

## Install everything for dev:
```bash
python -m venv .venv && source .venv/bin/activate.fish
pip install -e ".[dev]"
```

## Export pinned runtime deps for Docker (keeps images fast/reproducible):
```bash
pip freeze --exclude-editable  > requirements.txt
```

## 🧪 `pytest` (tests that are fast + friendly)
test discovery, asserts without boilerplate, fixtures.
1. create a `~/pytest.ini` - tells pytest where to look for tests (tests) and sets sane defaults
```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = --maxfail=1 -q
```

2. add `~/tests/conftest.py` - inserts src onto sys.path at test startup so imports like from src... work for both CLI pytest and VS Code discovery.
```python
from pathlib import Path
import sys

# Ensure src/ is on sys.path so imports like
# `from src.python_ci_pavedroad_template_app.app import app` work when
# running pytest from the repository root or when VS Code runs test discovery.
root = Path(__file__).resolve().parents[1]
src_dir = str(root / "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
```

3. add a `~/.vscode/settings.json` to enable pytest and points discovery at tests. In addition it configures the VS Code Python extension to use pytest and to discover tests from the tests folder.
```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests"
  ],
  "python.testing.unittestEnabled": false,
  "python.testing.autoTestDiscoverOnSaveEnabled": true,
  "python.testing.pytestPath": "pytest"
}
```
4. Add your tests under `~/tests/*` and run tests
```bash
pyest
#or
pytest --cov=src --cov-report=term -missing
```

## 🎨 Setup `black` (auto-format; zero bikeshedding)
enforces consistent formatting
```bash
# command line
black .
# CI run
black --check .

```
## 🪶 Setup `Ruff`
replaces multiple older tools (flake8, isort, pyupgrade, even parts of pylint) in one fast binary. “Black makes your code look good, Ruff makes it behave good.” Ruff is a linter and code fixer for Python written in Rust (blazing fast).
It checks your code against hundreds of rule families—for syntax errors, bad patterns, style issues, import order, etc.—and can auto-fix many of them.

- Configure Ruff inside your pyproject.toml It sets defaults so you (and CI) can just run ruff check . without flags.
```bash
ruff check .  # Lint Check (Only)
ruff check . -- fix # Auto Fix
ruff format . # CLI format
ruff check . --exit-zero  # always passes (for exploratory)
ruff check . --output-format=github  # nice PR comments

```

| Code     | Origin              | What it checks                                  |
| -------- | ------------------- | ----------------------------------------------- |
| `E`, `W` | **pycodestyle**     | Formatting (indentation, spacing, etc.)         |
| `F`      | **pyflakes**        | Undefined names, unused imports, syntax issues  |
| `I`      | **isort**           | Import sorting rules                            |
| `B`      | **flake8-bugbear**  | Logic errors and performance gotchas            |
| `UP`     | **pyupgrade**       | Modern Python syntax suggestions                |
| `N`      | **pep8-naming**     | Naming conventions for functions, classes, etc. |
| `S`      | **bandit**          | Security rules                                  |
| `C90`    | **mccabe**          | Cyclomatic complexity                           |
| `SIM`    | **flake8-simplify** | Simplify redundant patterns                     |
| `PL`     | **pylint subset**   | Some useful pylint checks                       |

## Add black and ruff to pre-commit hook locally & ci
1. Install + enable (fish shell)
```bash
source .venv/bin/activate.fish
pip install pre-commit
pre-commit install           # installs the git hook
pre-commit run --all-files   # run once across the whole repo
```
From now on, every git commit will run the hooks on staged files. If a hook fails, the commit is blocked until you fix and re-stage.
2. Add `pre-commit-config.yaml`
```ini
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: mixed-line-ending

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black
        language_version: python3.10
```
4. Typical loop when hook fails
```bash
pre-commit run --all-files   # see failures
ruff check . --fix           # auto-fix most issues
black .                      # format
git add -A                   # re-stage fixed files
git commit                   # try again
```
5. Keep hooks fresh
```bash
pre-commit autoupdate
git add .pre-commit-config.yaml
git commit -m "chore(pre-commit): autoupdate hooks"
```
6. Enforce in CI (so no bypass)
```yaml
name: CI

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  precommit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - name: Install pre-commit
        run: pip install pre-commit
      - name: Run pre-commit
        run: pre-commit run --all-files
```
Then in repo Settings → Branch protection:
- Require status checks to pass → check the precommit job.

Optional: use pre-commit.ci (super fast, auto-fixes on PRs). If enable it, keep the GitHub Action or rely solely on pre-commit.ci—either way, make the status required.

7. Nice-to-haves
- Speed up first run: `pre-commit clean` if caches get weird.
- Large files: add `--hook-stage manual` hooks if you want opt-in checks for big assets.
- Global default (optional): pre-commit init-templatedir ~/.git-template so new repos auto-get hooks.
