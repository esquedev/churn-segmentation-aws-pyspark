from unittest.mock import patch, MagicMock
from src.data_ingestion import ingest_data

@patch("src.data_ingestion.ingest_data.S3DataSource")
@patch("src.data_ingestion.ingest_data.SparkSessionFactory")
def test_main_runs_and_prints(mock_spark_factory, mock_s3datasource, capsys):
    mock_spark_factory.create.return_value = MagicMock()
    mock_s3datasource.return_value.read.return_value = "mocked data"
    ingest_data.main()
    captured = capsys.readouterr()
    assert "mocked data" in captured.out