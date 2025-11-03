#!/bin/fish

pre-commit run --all-files   # see failures
ruff check . --fix           # auto-fix most issues
black .                      # format
git add -A                   # re-stage fixed files
git commit                   # try again
