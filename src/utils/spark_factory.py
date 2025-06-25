from pyspark.sql import SparkSession

class SparkSessionFactory:
    """
    Factory pattern for creating SparkSession instances.
    """
    @staticmethod
    def create(app_name="Data Ingestion"):
        return SparkSession.builder.appName(app_name).getOrCreate()