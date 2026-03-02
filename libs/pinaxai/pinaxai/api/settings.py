from __future__ import annotations

from importlib import metadata

from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

from pinaxai.utils.log import logger


class PinaxAIAPISettings(BaseSettings):
    app_name: str = "pinaxai"
    app_version: str = "1.0.0"

    api_runtime: str = "prd"
    alpha_features: bool = False

    api_url: str = "http://localhost:8000"

    model_config = SettingsConfigDict(env_prefix="PINAXAI_")

    @field_validator("api_runtime", mode="before")
    def validate_runtime_env(cls, v):
        """Validate api_runtime."""

        valid_api_runtimes = ["dev", "stg", "prd"]
        if v.lower() not in valid_api_runtimes:
            raise ValueError(f"Invalid api_runtime: {v}")

        return v.lower()

    @field_validator("api_url", mode="before")
    def update_api_url(cls, v, info: ValidationInfo):
        api_runtime = info.data["api_runtime"]
        if api_runtime == "dev":
            from os import getenv

            if getenv("PINAXAI_RUNTIME") == "docker":
                return "http://host.docker.internal:8000"
            return "http://localhost:8000"
        elif api_runtime == "stg":
            return "http://localhost:8000"
        else:
            return "http://localhost:8000"

    def gate_alpha_feature(self):
        if not self.alpha_features:
            logger.error("This is an Alpha feature not for general use.")
            exit(1)


pinaxai_api_settings = PinaxAIAPISettings()
