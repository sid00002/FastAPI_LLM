from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI LLM Project"
    VERSION: str = "1.0.0"
    OPENAI_API_KEY: str | None = None  # we’ll use this later for LLM

    class Config:
        env_file = ".env"

settings = Settings()
