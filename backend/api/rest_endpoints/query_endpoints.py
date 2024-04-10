from fastapi.responses import RedirectResponse
from backend.api.api import app
from backend.api.kg_endpoints.kg_query import (get_concept_by_term,
                                               get_description,
                                               expand_node,
                                               get_data_properties,
                                               execute_sparql_query
                                               )


@app.get("/", tags=["CTOntoLib"])
async def root():
    return {"message": "Welcome to the CTOntoLib API. Please use the /docs endpoint to access the API documentation."}


@app.get("/search", tags=["CTOntoLib"])
async def search_term(term: str):
    """
    Search for classes in the Circular TwAIn Ontology Library
    """
    return get_concept_by_term(term)


@app.get("/description", tags=["CTOntoLib"])
async def get_description_by_uri(uri: str):
    """
    Get the annotation properties of a class in the Circular TwAIn Ontology Library
    """
    return get_description(uri)


@app.get("/data_properties", tags=["CTOntoLib"])
async def get_data_properties_by_uri(uri: str):
    """
    Get the data properties of a class in the Circular TwAIn Ontology Library
    """
    return get_data_properties(uri)


@app.get("/object_properties", tags=["CTOntoLib"])
async def get_object_properties_by_uri(uri: str):
    """
    Get the object properties of a class in the Circular TwAIn Ontology Library
    """
    return expand_node(uri)


@app.get("/sparql", tags=["sparql"])
async def sparql_query(query: str):
    """
    Query the SPARQL endpoint of the Circular TwAIn Ontology Library
    """
    return execute_sparql_query(query)
