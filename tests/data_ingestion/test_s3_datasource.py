from unittest.mock import MagicMock, patch
from src.data_ingestion.s3_datasource import S3DataSource

@patch("src.data_ingestion.s3_datasource.boto3.client")
def test_s3datasource_read(mock_boto_client):
    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3
    mock_s3.get_object.return_value = {
        'Body': MagicMock(read=MagicMock(return_value=b"test content"))
    }
    s3_source = S3DataSource(bucket_name="test-bucket", file_key="test-key")
    result = s3_source.read()
    assert result == "test content"
    mock_s3.get_object.assert_called_once_with(Bucket="test-bucket", Key="test-key")