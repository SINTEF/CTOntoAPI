import requests
import json
import re
import time
from util.log import logger
from typing import Any, List

from util.environment_and_configuration import (
    get_environment_variable,
)

class GraphDBQueryService:
    __instance = None
    __datastore = "CTOntoLib"


    #def __new__(cls):
    #    if cls.__instance is None:
    #        cls()
    #    return cls.__instance

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance


    def __init__(self):

        if self.__instance is not None:
            raise Exception("Singleton instantiated multiple times!")
      
        self.__sparql_endpoint = get_environment_variable("GRAPHDB_SPARQL_ENDPOINT")
        self.__auth_code = get_environment_variable("GRAPHDB_AUTH_CODE", optional=True, default="")
        self.__username = get_environment_variable("GRAPHDB_USERNAME", optional=True, default="admin")
        self.__password = get_environment_variable("GRAPHDB_PASSWORD", optional=True, default="root")
        self.__headers = {
            "Accept": "application/sparql-results+json",
            "Authorization": self.__auth_code,
        }


        GraphDBQueryService.__instance = self
        self.__connected = False
        self._connect()

    def _connect(self):
        
        self.__health_check_uri = f"{self.__sparql_endpoint}/health"
       

        while not self.__connected:
            try:
                logger.info("Connecting to GraphDB...")
                logger.info(f"Trying to connect to uri {self.__health_check_uri}.")

                response = requests.get(
                    self.__health_check_uri, headers=self.__headers, timeout=5, auth=(self.__username, self.__password)
                )
                if not response.ok:
                    raise Exception(f"Failed to connect to {self.__health_check_uri}. Response: {response.content}")

                self.__connected = True

                logger.info("Connected to GraphDB.")
            except Exception as e:
                logger.info(e)
                logger.info(
                    "GraphDB unavailable or Authentication invalid! Trying again in 10 seconds..."
                )
                time.sleep(10)

    def graphdb_get(self, sparql: any) -> Any:

        try:
            
            params = {"query": sparql}
            sparql_uri = self.__sparql_endpoint

            response = requests.get(sparql_uri, params=params, headers=self.__headers, auth=(self.__username, self.__password), timeout=5)
            if not response.ok:
                raise Exception(
                    f"Failed to query data from {self.__datastore}: {response.content}"
                )
            else:
                return response.json()

        except Exception as e:
            logger.info(e)