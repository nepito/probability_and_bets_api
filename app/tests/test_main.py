import pytest
import pandas as pd
from fastapi.testclient import TestClient

from app.main import app
from app.main import pandas_to_dict

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World from GECI!"}


EXPECTED = [{"a": [1, 2]}, {"a": [1, 2], "b": [3, 4]}, {"a": [1, 2], "b": [3, 4], "c": [5, 6]}]


@pytest.mark.parametrize("expected", EXPECTED)
def test_pandas_to_dict(expected):
    b = pd.DataFrame.from_dict(expected)
    c = pandas_to_dict(b)
    assert expected == c
