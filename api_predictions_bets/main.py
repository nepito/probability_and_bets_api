import requests
import pandas as pd
import json
from fastapi import FastAPI, Body

app = FastAPI()  # pragma: no mutate

league_season_round = "78_2021_16"
def get_matches(league_season_round):
    conn = requests.get(f"https://q98w4w.deta.dev/{league_season_round}")
    res = conn.json()
    bets = pd.DataFrame.from_dict(res)
    conn = requests.get(f"https://uxxery.deta.dev/{league_season_round}")
    res = conn.json()
    predicionts = pd.DataFrame.from_dict(res)
    matches = bets.join(predicionts.set_index("id_match"), on="id_match")
    return matches


def pandas_to_dict(a):
    return {columna: list(a[columna].values) for columna in a.columns}


def pandas_to_list_of_dict(a):
    return [a.iloc[i, :].to_dict() for i in range(len(a))]


@app.get("/{league_season_round}")
def read_root(league_season_round):
    matches = get_matches(league_season_round)
    to_render = pandas_to_list_of_dict(matches)
    return {"response": to_render}
