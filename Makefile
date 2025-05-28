# Makefile for anakin_library

.PHONY: help install dev clean test format lint

# Default help message
help:
	@echo "Usage:"
	@echo "  make install       Install the package in editable mode"
	@echo "  make dev           Install dev dependencies (tests, linters, etc.)"
	@echo "  make clean         Remove build and cache files"
	@echo "  make test          Run tests with pytest"
	@echo "  make format        Format code with black and isort"
	@echo "  make lint          Run flake8 and mypy"

# Install the library in editable mode
install:
	pip install -e .

# Install development tools (edit to match your needs)
dev:
	pip install -e ".[dev]"

# Clean Python cache, build artifacts, etc.
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache .mypy_cache dist build *.egg-info

# Run unit tests
test:
	pytest -v tests/

# Format code with black and isort
format:
	black src tests
	isort src tests

# Run linters
lint:
	flake8 src tests
	mypy src
