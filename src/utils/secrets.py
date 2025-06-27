import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv


class SecretProvider(ABC):
    @abstractmethod
    def get_secret(self, key: str, default=None):
        pass

class EnvSecretProvider(SecretProvider):
    def __init__(self):
        # Load .env file for local development
        load_dotenv()

    def get_secret(self, key: str, default=None):
        return os.environ.get(key, default)

# Factory pattern for extensibility
def get_secret_provider():
    # In the future, logic can be added here to select provider type
    return EnvSecretProvider()