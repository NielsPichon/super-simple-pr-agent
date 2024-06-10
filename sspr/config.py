import enum
import functools
import os
from typing import Any

import pydantic


class Provider(str, enum.Enum):
    """Possible LLM providers."""
    OPENAI = 'openai'
    OLLAMA = 'ollama'
    MISTRAL = 'mistral'


class Config(pydantic.BaseModel):
    """PR-agent configuration."""

    model: str = 'llama3'
    provider: str = 'ollama'
    api_base_url: str = 'http://localhost:11434'
    api_key: str = ''
    github_token: str = ''
    github_event_name: str = ''
    github_event_path: str = ''
    log_level: str = 'INFO'
    max_model_tokens: int = 4096

    def model_post_init(self, __context: Any):
        #Check the environment variables for possible overrides
        for attribute in self.model_dump():
            if attribute.upper() in os.environ:
                attr_type = type(getattr(self, attribute))
                parsed_value = attr_type(os.environ[attribute.upper()])
                setattr(self, attribute, parsed_value)

@functools.lru_cache(maxsize=1)
def get_config() -> Config:
    """Gets the system configuration from defaults and environment variables."""
    return Config()
