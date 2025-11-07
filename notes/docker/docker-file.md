🧠 Dockerfile Concept Overview

We bulding a multi-stage Dockerfile:
- Stage 1 (`builder`): install build tools, compile dependencies to “wheel” packages.
- Stage 2 (`runtime`): copy only what you need to run (the app + the built wheels).
    - → This gives you smaller, cleaner, faster containers.

⚙️ Step-by-Step Breakdown
1. **The directive**
```dockerfile
# syntax=docker/dockerfile:1.7
```
This tells Docker to use BuildKit features (like `--mount=cache` or heredoc syntax). Always keep this at the top when using modern dockerfiles.

2. **Base Image**
```dockerfile
FROM python:3:10-slim AS base
```
- Pulls a small Debian-based python image (~60MB)
- Maching python version ensures the code behaves the same inside / outside Docker
- `AS base` gives this stage a name so later stages can reuse it

3. **Environment Variables**
```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
```
| Var | Effect |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1` | Prevents `.pyc` cache files inside the container (less clutter) |
| `PYTHONUNBUFFERED=1` | Forces logs to flush immediately (good for Docker logs) |
| `PIP_NO_CACHE_DIR=1` | Doesn't leave pip's download cache on disk (saves image space) |

4. **Working directory**
```dockerfile
WORKDIR /app
```
- Sets the working directory for all subsequent commands
- `/app` is conventional for runtime images
- Docker will auto-create it if it doesn't exist

5. **Builder Stage**
```dockerfile
FROM base AS builder
```
This starts a new stage **using** base image layer, adding dev tools to build dependencies

**Install compiler + tools**
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl && \
    rm -rf /var/lib/apt/lists/*
```
- Needed for packages that compile native code (like `uvloop`, `psycopg2`, etc).
- `--no-install-recommends` keeps the layer / install light
- `rm -rf /var/lib/apt/lists/*` reduces image size by cleaning the cache

**Copy and build dependencies**
```dockerfile
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip wheel --wheel-dir /wheels -r requirements.txt
```
- Copies the dependency list into the builder
- Builds wheels (`.whl` files) into `/wheels` directory.
- Wheels are precompiled Python packages -- fast to install later and portable
- 🧠 **Wheels**: Installing from wheels in our next stage avoids re-downloading and recompiling -- so builds are fast and reproductable.

6. **RUNTIME stage**
By default containers run as **root** inside the container namespace.
- if an attacker escapes the container, they could become root on the host
- even inside the container, malicious code could modify system files, install packages, or access sensitive information in mounted volumes

Running as **non-root** user (ie: UID `10001`) reduced the blast radius.
- it limits the file permissions and prevents an attacker from escalating their priviledge
- it aligns with best practices for least privilege and security standards
- many platforms (Google cloud run, openshift) require them to run as non-root.
- `10001` means you cannot modify system directories or priviledged ports (<1024); you can safely execute app logic; best practice for modern containerized deployments.
