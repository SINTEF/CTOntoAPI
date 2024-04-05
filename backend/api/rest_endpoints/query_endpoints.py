from backend.api.api import app
from backend.api.kg_endpoints.kg_query import get_concept_by_term, get_description, expand_node

@app.get("/")
async def root():
    return {"message": "It works!"}


@app.get("/search")
async def search_term(term: str):
    return get_concept_by_term(term)

@app.get("/description")
async def get_description_by_uri(uri: str):
    print(uri)
    return get_description(uri)

@app.get("/expand")
async def expand_node_by_uri(uri: str):
    return expand_node(uri)