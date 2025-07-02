import boto3
from .base import ConfigProvider

class SSMParameterProvider(ConfigProvider):
    def __init__(self, region_name="us-east-1"):
        self.ssm = boto3.client("ssm", region_name=region_name)

    def get_config(self, key: str, default=None):
        try:
            response = self.ssm.get_parameter(Name=key, WithDecryption=True)
            return response["Parameter"]["Value"]
        except self.ssm.exceptions.ParameterNotFound:
            return default