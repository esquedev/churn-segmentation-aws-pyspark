from utils.spark_factory import SparkSessionFactory
from .s3_datasource import S3DataSource

def main():
    # Dependency Inversion: main depends on abstractions, not concrete classes.
    spark = SparkSessionFactory.create()
    data_source = S3DataSource(bucket_name="example-bucket", file_key="data/raw/sample.csv")
    data = data_source.read()
    print(data)

if __name__ == "__main__":
    main()