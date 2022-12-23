import cohere
import pandas as pd
from annoy import AnnoyIndex

from .settings import API_KEY
from .utils import get_data

# Create and retrieve a Cohere API key from os.cohere.ai
co = cohere.Client(API_KEY)

search_index = AnnoyIndex(4096, 'angular')
search_index.load('embeddings.ann')

data = get_data()

def get_similar_results(query):

    query_embed = co.embed(
        texts=[query],
        model="large",
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
            'texts': data.iloc[similar_item_ids[0]]['title'],
            'distance': similar_item_ids[1],
        },
    )

    results.reset_index(drop=True, inplace=True)
    return results
