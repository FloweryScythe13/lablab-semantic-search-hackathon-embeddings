import json
import logging 

import pandas as pd

from settings import DATA_PATH

def get_data():
    try:
        
        with open(DATA_PATH, encoding="utf-8") as f:
            data = json.load(f)

        data = pd.DataFrame(data=data)
        assert data.shape[0] > 0
        data = data[data['title'].notna()]
        data = data.drop_duplicates("title")

        return data
    except Exception as ex:
        logging.debug(ex)
