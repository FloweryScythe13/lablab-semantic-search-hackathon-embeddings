import cohere
import logging 
import pandas as pd
from annoy import AnnoyIndex
from pathlib import Path

from settings import API_KEY
from settings import EMBEDDINGS_PATH
from utils import get_data

# Create and retrieve a Cohere API key from os.cohere.ai
try:
    co = cohere.Client(API_KEY)

    search_index = AnnoyIndex(768, 'angular')
    logging.info(f"First: {Path(__file__)}")
    logging.info(f"Second: {Path(__file__).parent}")
    logging.info(f"Third: {Path(__file__).parent.joinpath('sample_data', 'Latest_News.json')}")
    logging.info(f"Fourth: {Path(__file__).parent.joinpath('embeddings', 'embeddings.ann')}")
    print(f"EMBEDDINGS_PATH {EMBEDDINGS_PATH}")
    search_index.load(EMBEDDINGS_PATH)

    data = get_data()
except Exception as ex:
    print(ex)

def get_similar_results(query):

    query_embed = co.embed(
        texts=[query],
        model="multilingual-22-12",
        truncate="LEFT",
    ).embeddings

    # Retrieve the nearest neighbors
    similar_item_ids = search_index.get_nns_by_vector(
        query_embed[0],10,
        include_distances=True,
    )
    # Format the results
    results = pd.DataFrame(
        data={
            'Relevant articles': data.iloc[similar_item_ids[0]]['title'],
            # 'distance': similar_item_ids[1],
            'Links': data.iloc[similar_item_ids[0]]['link'],
        },
    )

    results.reset_index(drop=True, inplace=True)
    return results
