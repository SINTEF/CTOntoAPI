import fastapi
from util.environment_and_configuration import get_environment_variable, get_configuration, ConfigGroups

from util.log import logger

"""
Fast API
Separated from service.py to avoid circular dependencies with endpoint files importing the "app" instance. 
"""
#root_path = get_environment_variable(key="API_ROOT_PATH", default="/")
#openapi_path = get_environment_variable(key="OPENAPI_URL", default="/openapi.json")
#logger.info(f"API: Root path set to: {root_path}")
#logger.info(f"API: Openapi path set to: {openapi_path}")
#app = fastapi.FastAPI(root_path=root_path, openapi_url=openapi_path)
description = """
This is a smiple API for querying the data from the Circular TwAIn Ontology Library and Wikidata.
For quering WikiData, the API uses the [LamAPI](https://lamapi.hel.sintef.cloud/).
"""

tags_metadata = [
    {
        "name": "CTOntoLib",
        "description": "Query the Circular TwAIn Ontology Library.",
    },
    {
        "name": "wikidata",
        "description": "Query Wikidata.",
    },
    {
        "name": "sparql",
        "description": "Query the SPARQL endpoint of the Circular TwAIn Ontology Library.",
    },
]

api_version = get_configuration(ConfigGroups.API, "api_version")
app = fastapi.FastAPI(
    title="Circular TwAIn Ontology Library API",
    description=description,
    version=api_version,
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=tags_metadata,


)

""" def custom_openapi():
    if not app.openapi_schema:
        
        app.openapi_schema = fastapi.openapi.utils.get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get('paths').items():
            for _, param in method_item.items():
                responses = param.get('responses')
                # remove 422 response, also can remove other status code
                if '422' in responses:
                    del responses['422']
    return app.openapi_schema

app.openapi = custom_openapi """