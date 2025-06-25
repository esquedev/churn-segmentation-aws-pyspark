from src.utils.spark_factory import SparkSessionFactory

def test_create_spark_session(monkeypatch):
    class DummySparkSession:
        @staticmethod
        def builder():
            class Builder:
                def appName(self, name):
                    return self
                def getOrCreate(self):
                    return "dummy_spark_session"
            return Builder()
    monkeypatch.setattr("src.utils.spark_factory.SparkSession", DummySparkSession)
    session = SparkSessionFactory.create()
    assert session == "dummy_spark_session"