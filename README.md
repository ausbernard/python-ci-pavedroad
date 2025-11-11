# Paved Road CI for Python Applications

A reusable, production-ready **CI/CD pipeline** template for Python projects — built with **GitHub Actions**, **Docker**, and **best practices** in testing, linting, and deployment.

You can drop this **workflow** into any Python project.

---

## 🚀 Features

- ✅ Automated testing with **pytest**
- ✅ Code quality enforcement via **black** + **ruff**
- ✅ Multi-stage Docker builds
- ✅ CI/CD via **GitHub Actions**
- ✅ Push Docker image to **GitHub Container Registry (GHCR)**
- ✅ Example deployment via **Docker Compose**

---

## 🧱 Tech Stack

| Tool | Purpose |
|------|----------|
| 🐍 Python 3.11 | Application logic |
| 🧪 pytest | Unit testing |
| 🎨 black + ruff | Linting & formatting |
| 🐳 Docker / Docker Compose | Containerization & local deployment |
| ⚙️ GitHub Actions | Continuous Integration & Delivery |
| ☁️ GHCR | Container image hosting |

---

## 🏃‍♂️ Quick Start
*coming soon*

## 🏗️ Repository Structure

```bash
python-ci-pavedroad/
├── .github/
│   └── workflows/
│       └── python-deploy.yaml            # CI pipeline
├── src/
│   └── app.py                # Sample app
├── tests/
│   └── test_health.py           # Unit tests
│   └── test_root.py           # Unit tests
├── Dockerfile
├── .dockerignore
├── pyproject.toml
├── requirements.txt          # Python dependencies
├── .pre-commit-config.yaml
├── .gitignore
└── README.md
