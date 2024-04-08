from backend.api.api import app
from backend.api.kg_endpoints.kg_query import (get_concept_by_term,
                                               get_description,
                                               expand_node,
                                               get_data_properties,
                                               )


@app.get("/")
async def root():
    return {"message": "It works!"}


@app.get("/search")
async def search_term(term: str):
    return get_concept_by_term(term)


@app.get("/description")
async def get_description_by_uri(uri: str):
    return get_description(uri)


@app.get("/data_properties")
async def get_data_properties_by_uri(uri: str):
    return get_data_properties(uri)


@app.get("/expand")
async def expand_node_by_uri(uri: str):
    return expand_node(uri)
