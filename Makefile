install:
	uv sync

build:
	uv build

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check . --fix