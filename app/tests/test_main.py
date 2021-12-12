import pytest
import pandas as pd
from fastapi.testclient import TestClient

from app.main import app
from app.main import pandas_to_dict, pandas_to_list_of_dict

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


EXPECTED = [
    ({"a": [1, 2]}, [{"a": 1}, {"a": 2}]),
    ({"a": [1, 2], "b": [3, 4]}, [{"a": 1, "b": 3}, {"a": 2, "b": 4}]),
    ({"a": [1, 2, 5], "b": [3, 4, 6]}, [{"a": 1, "b": 3}, {"a": 2, "b": 4}, {"a": 5, "b": 6}]),
    ({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, [{"a": 1, "b": 3, "c": 5}, {"a": 2, "b": 4, "c": 6}]),
]


@pytest.mark.parametrize("dict_of_list, expected_list", EXPECTED)
def test_pandas_to_list_of_dict(dict_of_list, expected_list):
    b = pd.DataFrame.from_dict(dict_of_list)
    c = pandas_to_list_of_dict(b)
    assert expected_list == c
    a = {"a": [1, 2], "b": [3, 4]}
    b = pd.DataFrame.from_dict(a)
    c = pandas_to_list_of_dict(b)
    expected_list = [{"a": 1, "b": 3}, {"a": 2, "b": 4}]
    assert expected_list == c
