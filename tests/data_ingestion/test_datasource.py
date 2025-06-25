from src.data_ingestion.datasource import DataSource

class DummyDataSource(DataSource):
    def read(self):
        return "dummy data"

def test_datasource_abstraction():
    ds = DummyDataSource()
    assert ds.read() == "dummy data"