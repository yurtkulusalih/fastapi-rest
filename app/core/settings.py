import logging
from typing import Any
from pydantic import BaseSettings, PostgresDsn 

class AppSettings(BaseSettings):
    debug: bool = True
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI boilerplate"
    version: str = "0.0.0"

    database_url: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10


    api_prefix: str = "/api"

    jwt_token_prefix: str = "Token"

    allowed_hosts: list[str] = ["*"]

    logging_level: int = logging.DEBUG
    loggers: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        env_file = ".env" # Can be moved under `BaseAppSettings` later
        validate_assignment = True

    @property
    def fast_api_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }