from backend.api.api import app
from backend.api.kg_endpoints.wikidata_query import (entity_retrival, get_labels
)

@app.get("/wikidata/search", tags=["wikidata"])
async def wikidata_search_term(term: str):
    """
    Search for entities in Wikidata
    """
    return entity_retrival(term)

@app.get("/wikidata/labels", tags=["wikidata"])
async def wikidata_get_labels_by_uri(uri: str):
    """
    Get labels from Wikidata
    """
    return get_labels(uri)