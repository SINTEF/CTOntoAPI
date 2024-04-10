import uvicorn
from backend.semantic_knowledge_graph.GraphDB_query_service import GraphDBQueryService
from util.log import logger
from backend.api.api import app

from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
)

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