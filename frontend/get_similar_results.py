import cohere
import logging 
import pandas as pd
from annoy import AnnoyIndex
from pathlib import Path

import settings

from utils import get_data

# Create and retrieve a Cohere API key from os.cohere.ai
class SearchEngine:
    def __init__(self) -> None:
        self.co = cohere.Client(settings.API_KEY)

        self.search_index = AnnoyIndex(4096, 'angular')
        self.search_index.load(settings.EMBEDDINGS_PATH)
        self.data = get_data()
        
    def get_similar_results(self, query):

        query_embed = self.co.embed(
            texts=[query],
            model="multilingual-22-12",
            truncate="LEFT",
        ).embeddings

        # Retrieve the nearest neighbors
        similar_item_ids = self.search_index.get_nns_by_vector(
            query_embed[0],10,
            include_distances=True,
        )
        # Format the results
        results = pd.DataFrame(
            data={
                'Relevant articles': self.data.iloc[similar_item_ids[0]]['title'],
                # 'distance': similar_item_ids[1],
                'Links': self.data.iloc[similar_item_ids[0]]['link'],
            },
        )

        results.reset_index(drop=True, inplace=True)
        return results
