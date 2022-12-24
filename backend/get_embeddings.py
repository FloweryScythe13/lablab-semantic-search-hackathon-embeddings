import cohere
import pandas as pd
from .utils import get_data
from .settings import API_KEY
from annoy import AnnoyIndex
from time import sleep
data = get_data()

df = pd.DataFrame(data)

co = cohere.Client(api_key=API_KEY)
co.batch_size = 96
search_index = AnnoyIndex(4096, 'angular')
rate_limit_batch = 4800
for i in range(0, df.shape[0], rate_limit_batch):
    rows = df.iloc[i:i+rate_limit_batch]
    embeds = co.embed(texts=list(rows['title']), 
                  model='large',
                  truncate='NONE').embeddings
    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])
    sleep(41)
    
search_index.build(10)
search_index.save('test.ann')
    