from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "forestin-meta"
    app_env: str = "development"
    api_key: str = "forestin-meta-poc"

    meta_mode: Literal["mock", "live"] = "mock"
    meta_graph_version: str = "v23.0"
    meta_access_token: str | None = None
    meta_facebook_page_id: str | None = None
    meta_instagram_account_id: str | None = None
    meta_threads_user_id: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
