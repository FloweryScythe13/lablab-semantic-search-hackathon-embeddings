import cohere
import pandas as pd
from annoy import AnnoyIndex

from settings import API_KEY
from settings import EMBEDDINGS_PATH
from utils import get_data

# Create and retrieve a Cohere API key from os.cohere.ai
co = cohere.Client(API_KEY)

search_index = AnnoyIndex(768, 'angular')
print(f"EMBEDDINGS_PATH {EMBEDDINGS_PATH}")
search_index.load(EMBEDDINGS_PATH)

data = get_data()

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
