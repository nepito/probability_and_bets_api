import pandas as pd
import json
from fastapi import FastAPI, Body

app = FastAPI()  # pragma: no mutate

league_season_round = "78_2021_15"
path_1 = f"data/bets_{league_season_round}.csv"
path_2 = f"data/predictions_{league_season_round}.csv"
bets = pd.read_csv(path_1)
predicionts = pd.read_csv(path_2)
matches = bets.join(predicionts.set_index("id_match"), on="id_match")
to_render = [matches.iloc[i, :].to_dict() for i in range(len(matches))]


def pandas_to_dict(a):
    return {columna: list(a[columna].values) for columna in a.columns}


def pandas_to_list_of_dict(a):
    return [a.iloc[i, :].to_dict() for i in range(len(a))]


@app.get("/")
def read_root():
    return {"msg": "Hello World from GECI!"}
