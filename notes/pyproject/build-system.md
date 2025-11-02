# Hatching
Hatchling is often the preferred choice for new Python projects due to its modern features and compliance with current standards. It allows developers to leverage modern standards without needing deeply integrated configurations.

## Adavantages
- **Standards Compliance**: It adheres to PEP 517 and PEP 621, which are modern standards for Python packaging
    - **PEP 517 (Build System Interface)**: Defines the standard interface between Python package management tools and the build system that package projects. It separates the build process from the installation process which allows for flexibility. Create and use alt tools outside of traditional `setuptools`. It allows for users to build your project without worrying about specific tools.
    - **PEP 621 (Metadata for Python Projects)**: Standarized way to present project metadata in `pyproject.toml`. Specifies the fields to include, name, version, authors, license, and dependencies. Helps package tools easily and access important information.

- **Extensibility**: Hatching supports build hooks, allowing for customization during the build process
- **Active Maintenance**: It is maintained under Python Packing Authority (PyPA), ensuing ongoing support and updates.

## Alternatives to Hatchling

While Hatchling is a strong choice, there are other build backends available:

| Backend | Description |
|---|---|
| setuptools | Widely used but less modern; not recommended for new projects. |
| flit | Minimal backend, lacks some features like editable installs. |
| poetry-core | Tied to the Poetry tool, better for applications than libraries. |
| pdm-backend | Similar to Poetry, but less widely adopted. |
| meson-python | Suitable for complex projects with non-Python dependencies. |
| scikit-build | Designed for projects needing advanced build configurations. |

## Explanations
[build-system]: lets tools know how to build your project (Hatchling = lightweight, modern).

[project]: PEP 621 metadata + runtime dependencies (just fastapi + uvicorn here).

[project.optional-dependencies].dev: everything you use during development (tests, lint, format, hooks, types).

[tool.black]: formatting rules (line length, python version, what to ignore).

[tool.ruff]: fast linting + import sorting (basic rule sets to start).

[tool.pytest.ini_options]: pytest defaults so you can just run pytest.

[tool.mypy]: typing checks (optional; enabled but not strict).
