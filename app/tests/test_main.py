import pandas as pd
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World from GECI!"}

def test_pandas_to_dict():
    a = {"a": [1,2]}
    b = pd.DataFrame.from_dict(a)
    c = pandas_to_dict(b)
    pass
