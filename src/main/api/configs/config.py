from pathlib import Path
from typing import Any

class Config:
    _isinstance = None
    _dictionary_ = {}

    def __new__(cls):
        if cls._isinstance is None:
            cls._isinstance = super(Config, cls).__new__(cls)

            config_path = Path(__file__).parents[4] / 'resources' / 'urls.properties'

            if not config_path.exists():
                raise FileNotFoundError(f"Config file not found: {config_path}")

            with open(config_path, "r") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.split("=")
                        key = key.strip()
                        value = value.strip()
                        cls._dictionary_[key] = value.strip()


        return cls._isinstance

    @classmethod
    def fetch(cls, key: str, default_value: Any = None) -> Any:
        return Config()._dictionary_.get(key, default_value)