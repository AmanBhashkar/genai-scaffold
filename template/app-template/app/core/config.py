from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "{{ project_name }}"
    DATABASE_URL: str = "{% if database == 'postgres' %}postgresql+asyncpg://user:password@localhost/{{ project_name }}{% else %}mongodb://localhost:27017/{{ project_name }}{% endif %}"
    
    # LLM Configuration
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None
    
    # Observability
    ENABLE_LANGSMITH: bool = {{ enable_langsmith | lower }}
    LANGCHAIN_TRACING_V2: str = "true" if {{ enable_langsmith | lower }} else "false"
    LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGCHAIN_API_KEY: Optional[str] = None
    LANGCHAIN_PROJECT: str = "{{ project_name }}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
