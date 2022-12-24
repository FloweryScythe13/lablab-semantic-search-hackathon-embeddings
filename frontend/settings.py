from decouple import config
from pathlib import Path

project_root = Path(__file__).parent.parent
DATA_PATH = config("DATA_PATH", default=str(project_root.joinpath("sample_data", "Latest_News.json")))
# DATA_PATH = config("DATA_PATH", default="/app/lablab-semantic-search-hackathon-embeddings/sample_data/Latest_News.json")

# add API_KEY in .env file
API_KEY = config("API_KEY")

 
EMBEDDINGS_PATH = config("EMBEDDINGS_PATH", default=str(project_root.joinpath("embeddings", "embeddings.ann")))
# EMBEDDINGS_PATH = config("EMBEDDINGS_PATH", default="/app/lablab-semantic-search-hackathon-embeddings/embeddings/embeddings_v1.ann")
