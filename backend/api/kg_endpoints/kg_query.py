from backend.semantic_knowledge_graph.GraphDB_query_service import GraphDBQueryService



term_search_query_file = "backend/semantic_knowledge_graph/query/term_search.spqrl"
get_description_query_file = "backend/semantic_knowledge_graph/query/get_description.sparql"
expand_node_query_file = "backend/semantic_knowledge_graph/query/expand_node.sparql"
get_data_properties_query_file = "backend/semantic_knowledge_graph/query/get_data_properties.sparql"

def get_concept_by_term(term: str) -> list:
    # Read the sparql query from a file
    with open(term_search_query_file, "r") as file:
        sparql = file.read().replace("[SearchTerm]", term)

    return_values = []

    graphdb_service = GraphDBQueryService.instance()
    results =  graphdb_service.graphdb_get(sparql)
    if (
        results is not None
        and results["results"] is not None
        and results["results"]["bindings"] is not None
        and len(results["results"]["bindings"]) > 0
    ):

        bindings = results["results"]["bindings"]
        for binding in bindings:
           uri = binding["documentID"]["value"]
           score = binding["maxscore"]["value"]
           return_values.append({"uri": uri, "score": score})
    
    return return_values

def get_description(uri: str) -> list:
    # Read the sparql query from a file
    with open(get_description_query_file, "r") as file:
        sparql = file.read().replace("[SearchSubject]", uri)

    #print(sparql)
    return_values = []

    graphdb_service = GraphDBQueryService.instance()
    results = graphdb_service.graphdb_get(sparql)
    #print(results)
    if (
        results is not None
        and results["results"] is not None
        and results["results"]["bindings"] is not None
        and len(results["results"]["bindings"]) > 0
    ):
        bindings = results["results"]["bindings"]
        for binding in bindings:
            #print(binding)
            description_type = binding["p"]["value"]
            description = binding["o"]["value"]
            return_values.append({description_type: description})
    
    return return_values

def get_data_properties(uri: str) -> list:
    # Read the sparql query from a file
    with open(get_data_properties_query_file, "r") as file:
        sparql = file.read().replace("[SearchSubject]", uri)

    #print(sparql)
    return_values = []

    graphdb_service = GraphDBQueryService.instance()
    results = graphdb_service.graphdb_get(sparql)
    #print(results)
    if (
        results is not None
        and results["results"] is not None
        and results["results"]["bindings"] is not None
        and len(results["results"]["bindings"]) > 0
    ):
        bindings = results["results"]["bindings"]
        for binding in bindings:
            #print(binding)
            description_type = binding["p"]["value"]
            description = binding["o"]["value"]
            return_values.append({description_type: description})
    
    return return_values

def expand_node(uri: str) -> dict:
    # Read the sparql query from a file
    with open(expand_node_query_file, "r") as file:
        sparql = file.read().replace("[SearchSubject]", uri)

    return_values = []
    outgoing = []
    incoming = []

    graphdb_service = GraphDBQueryService.instance()
    results = graphdb_service.graphdb_get(sparql)
    if (
        results is not None
        and results["results"] is not None
        and results["results"]["bindings"] is not None
        and len(results["results"]["bindings"]) > 0
    ):
        bindings = results["results"]["bindings"]
        for binding in bindings:
            #print(binding)
            if "o" in binding:
                property = binding["p"]["value"]
                object = binding["o"]["value"]
                outgoing.append({"property": property, "object": object})
            elif "s" in binding:
                property = binding["p"]["value"]
                subject = binding["s"]["value"]
                incoming.append({"property": property, "subject": subject})
    
    return_values = {"outgoing": outgoing, "incoming": incoming}
    return return_values


def execute_sparql_query(query: str) -> dict:
    graphdb_service = GraphDBQueryService.instance()
    results = graphdb_service.graphdb_get(query)
    return results