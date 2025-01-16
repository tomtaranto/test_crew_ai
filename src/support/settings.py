from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    gcp_project_id: str
    gcp_location: str
    vertex_ai_model: str


@lru_cache()
def settings() -> Settings:
    load_dotenv()
    return Settings()

