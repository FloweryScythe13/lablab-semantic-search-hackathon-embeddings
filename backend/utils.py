import json

import pandas as pd

from .settings import DATA_PATH

def get_data():

    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)

    data = pd.DataFrame(data=data)
    return data
