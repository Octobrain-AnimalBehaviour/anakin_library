# Anakin Library
A Python library that wraps ChromaDB and embeddings with custom vector DB

## Makefile
This project uses a `Makefile` to simplify common development tasks. Below is a breakdown of each available command:

`make install`

Installs the library in editable mode using pip:

> pip install -e .

This lets you modify the source code and immediately see changes without reinstalling.

`make dev`

Installs development dependencies like testing, linting, and formatting tools. These help with code quality and running tests:

pip install -e ".[dev]"

`make clean`

Removes build artifacts and cache files that Python and build tools generate, such as:

- __pycache__/

- .pytest_cache/

- .mypy_cache/

- dist/ and build/ folders

- *.egg-info/ directories

Use this command to clean your workspace and avoid stale files interfering with builds or tests.

`make test`

Runs the test suite using pytest:

> pytest -v tests/

This executes unit tests and provides verbose output.

`make format`

Automatically formats your Python code using tools like:

- Black — code formatter

- isort — import sorter

Running this command helps keep code style consistent and clean.

`make lint`

Runs static analysis tools to catch style and type errors:

- flake8 — style and quality checks

- mypy — static type checking

This helps maintain code quality and catch bugs early.

### How to Use

Run any command with:

> make <command>

For example:

> make install
