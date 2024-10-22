from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
    get_environment_variable_bool,
)

#if not running in docker, load environment variables from dev .env file
if not get_environment_variable_bool("DOCKER_ENV", optional=True, default=False):
    from dotenv import load_dotenv
    load_dotenv("environment_and_configuration/dev_environment_backend.env")


import uvicorn
from backend.semantic_knowledge_graph.GraphDB_query_service import GraphDBQueryService
from util.log import logger
from backend.api.api import app



from backend.api.rest_endpoints import (query_endpoints, 
                                        wikidata_endpoints)


if __name__ == "__main__":
    logger.info("Initializing backend...")

    graphdb_service = GraphDBQueryService()
    logger.info("Done initializing Knowledge GraphDB.")

    # Run fast API
    logger.info("Running FastAPI...")
    uvicorn.run(
        "run_backend:app",
        host=get_environment_variable("FAST_API_HOST"),
        port=get_environment_variable_int("FAST_API_PORT"),
        workers=1,
        access_log=True,
    )