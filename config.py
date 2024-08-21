import json
from json import JSONDecodeError
from typing import Any, Dict

class ConfigLoader:
    """A class for loading configuration data such as messages and statuses."""

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the config loader by loading the configuration file.

        :param config_path: Path to the configuration file.
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                self._config: Dict[str, Any] = json.load(file)
        except (FileNotFoundError, JSONDecodeError) as e:
            print(f"File upload error: {e}")
            self._config = {}

    def get(self, key: str) -> Any | None:
        """
        Get a value from the configuration using the provided key.

        :param key: The key to search in the configuration.
        :return: The corresponding value or None if the key is not found.
        """
        return self._config.get(key, None)