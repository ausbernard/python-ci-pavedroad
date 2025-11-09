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

## 🏗️ Repository Structure

```bash
python-ci-pavedroad/
├── .github/
│   └── workflows/
│       └── python-deploy-np.yaml            # CI pipeline
        └── python-promote.yaml            # CI pipeline
        └── python-deploy-pr.yaml            # CI pipeline
├── src/
│   └── app.py                # Sample app
├── tests/
│   └── test_app.py           # Unit tests
├── Dockerfile                # Multi-stage Docker build
├── docker-compose.yml        # Local deployment
├── requirements.txt          # Python dependencies
└── README.md
2025-11-08T23:52:23-05:00 bump test
