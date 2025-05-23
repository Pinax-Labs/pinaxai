from __future__ import annotations

from importlib import metadata
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

from pinaxai.utils.log import logger

PINAXAI_CLI_CONFIG_DIR: Path = Path.home().resolve().joinpath(".config").joinpath("pa")


class PinaxaiCliSettings(BaseSettings):
    app_name: str = "pinaxai"
    app_version: str = metadata.version("pinaxai")

    tmp_token_path: Path = PINAXAI_CLI_CONFIG_DIR.joinpath("tmp_token")
    config_file_path: Path = PINAXAI_CLI_CONFIG_DIR.joinpath("config.json")
    credentials_path: Path = PINAXAI_CLI_CONFIG_DIR.joinpath("credentials.json")
    ai_conversations_path: Path = PINAXAI_CLI_CONFIG_DIR.joinpath("ai_conversations.json")
    auth_token_cookie: str = "__pinaxai_session"
    auth_token_header: str = "X-PINAXAI-AUTH-TOKEN"

    api_runtime: str = "prd"
    api_enabled: bool = True
    alpha_features: bool = False
    api_url: str = Field("https://api.pinax.tech", validate_default=True)
    signin_url: str = Field("https://app.pinax.tech/login", validate_default=True)
    playground_url: str = Field("https://app.pinax.tech/playground", validate_default=True)

    model_config = SettingsConfigDict(env_prefix="PINAXAI_")

    @field_validator("api_runtime", mode="before")
    def validate_runtime_env(cls, v):
        """Validate api_runtime."""

        valid_api_runtimes = ["dev", "stg", "prd"]
        if v.lower() not in valid_api_runtimes:
            raise ValueError(f"Invalid api_runtime: {v}")

        return v.lower()

    @field_validator("signin_url", mode="before")
    def update_signin_url(cls, v, info: ValidationInfo):
        api_runtime = info.data["api_runtime"]
        if api_runtime == "dev":
            return "http://localhost:3000/login"
        elif api_runtime == "stg":
            return "https://app-stg.pinax.tech/login"
        else:
            return "https://app.pinax.tech/login"

    @field_validator("playground_url", mode="before")
    def update_playground_url(cls, v, info: ValidationInfo):
        api_runtime = info.data["api_runtime"]
        if api_runtime == "dev":
            return "http://localhost:3000/playground"
        elif api_runtime == "stg":
            return "https://app-stg.pinax.tech/playground"
        else:
            return "https://app.pinax.tech/playground"

    @field_validator("api_url", mode="before")
    def update_api_url(cls, v, info: ValidationInfo):
        api_runtime = info.data["api_runtime"]
        if api_runtime == "dev":
            from os import getenv

            if getenv("PINAXAI_RUNTIME") == "docker":
                return "http://host.docker.internal:7070"
            return "http://localhost:7070"
        elif api_runtime == "stg":
            return "https://api-stg.pinax.tech"
        else:
            return "https://api.pinax.tech"

    def gate_alpha_feature(self):
        if not self.alpha_features:
            logger.error("This is an Alpha feature not for general use.\nPlease message the Pinaxai team for access.")
            exit(1)


pinaxai_cli_settings = PinaxaiCliSettings()
