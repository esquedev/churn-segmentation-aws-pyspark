import boto3
from .datasource import DataSource

class S3DataSource(DataSource):
    """
    Concrete implementation of DataSource for AWS S3.
    """
    def __init__(self, bucket_name, file_key, aws_region='us-east-1'):
        self.bucket_name = bucket_name
        self.file_key = file_key
        self.s3 = boto3.client('s3', region_name=aws_region)

    def read(self):
        response = self.s3.get_object(Bucket=self.bucket_name, Key=self.file_key)
        return response['Body'].read().decode('utf-8')