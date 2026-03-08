# {{ project_name }}

{{ description }}

## Getting Started

1.  **Install uv**: If you haven't already, install [uv](https://github.com/astral-sh/uv).
2.  **Clone the repository**: `git clone <repo-url>`
3.  **Setup environment**:
    ```bash
    cp .env.example .env
    # Add your API keys and configuration
    ```
4.  **Run development server**:
    ```bash
    make dev
    ```
    Or using `uv` directly:
    ```bash
    uv sync
    uv run fastapi dev app/main.py
    ```

## Project Structure

- `app/`: Main application code.
  - `api/`: API endpoints and routers.
  - `core/`: Core logic (config, database, security).
  - `services/`: Business logic services (e.g., GenAI service).
- `Dockerfile`: Production Docker build.
- `Makefile`: Common development tasks.
- `pyproject.toml`: Dependency management via `uv`.

## Observability

- **LangSmith**: Enabled if `ENABLE_LANGSMITH` is set to `true` in your `.env`.
- **OpenTelemetry**: Integrated with FastAPI for request tracing.

## License

MIT
