# Stage 1: Builder
FROM python:{{ python_version }}-slim as builder

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files
copy pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Stage 2: Runtime
FROM python:{{ python_version }}-slim

WORKDIR /app

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy the application code
COPY . .

# Run the application
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
