import os
from .base import ConfigProvider

class EnvConfigProvider(ConfigProvider):
    def get_config(self, key: str, default=None):
        return os.environ.get(key, default)