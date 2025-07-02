import logging
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from src.data_ingestion.datasource import DataSource
from src.utils.secrets import SecretProvider, get_secret_provider
from src.utils.config.factory import get_config_provider
from src.utils.config.base import ConfigProvider

logger = logging.getLogger(__name__)

class S3DataSource(DataSource):
    """
    DataSource implementation for reading data from AWS S3,
    retrieving credentials (secrets) and parameters (config) from providers.
    """

    def __init__(
        self,
        bucket_name: str = None,
        file_key: str = None,
        aws_region: str = None,
        secret_provider: SecretProvider = None,
        config_provider: ConfigProvider = None,
    ):
        """
        Initialize the S3DataSource.

        Args:
            bucket_name (str, optional): Name of the S3 bucket (parameter).
            file_key (str, optional): Key of the file to read (parameter).
            aws_region (str, optional): AWS region (parameter).
            secret_provider (SecretProvider, optional): Provider for AWS credentials.
            config_provider (ConfigProvider, optional): Provider for config parameters.
        """
        self.secret_provider = secret_provider or get_secret_provider()
        self.config_provider = config_provider or get_config_provider()
        # Parameters (non-sensitive)
        self.bucket_name = bucket_name or self.config_provider.get_config("S3_BUCKET_NAME")
        self.file_key = file_key or self.config_provider.get_config("S3_FILE_KEY")
        self.aws_region = aws_region or self.config_provider.get_config("AWS_REGION", "us-east-1")
        # Secrets (sensitive)
        aws_access_key_id = self.secret_provider.get_secret("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = self.secret_provider.get_secret("AWS_SECRET_ACCESS_KEY")

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=self.aws_region,
        )

    def read(self) -> str:
        """
        Read the file from S3 and return its contents as a string.

        Returns:
            str: File contents.

        Raises:
            Exception: If the file cannot be read.
        """
        try:
            logger.info(f"Reading {self.file_key} from bucket {self.bucket_name}")
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.file_key)
            data = response["Body"].read().decode("utf-8")
            logger.info(f"Successfully read {self.file_key} from bucket {self.bucket_name}")
            return data
        except (BotoCoreError, ClientError) as e:
            logger.error(f"Failed to read {self.file_key} from bucket {self.bucket_name}: {e}")
            raise