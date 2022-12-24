from decouple import config


DATA_PATH = config("DATA_PATH", default=Path(__file__).parent.joinpath("sample_data", "Latest_News.json"))

# add API_KEY in .env file
API_KEY = config("API_KEY")

# 
EMBEDDINGS_PATH = config("EMBEDDINGS_PATH", default=Path(__file__).parent.joinpath("embeddings", "embeddings.ann"))
