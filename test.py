

from backend.api.kg_endpoints.kg_query import get_concept_by_term, get_description, expand_node
import json

if __name__ == "__main__":
    results = expand_node("http://qudt.org/vocab/quantitykind/Temperature")
    
    #pretty print the json results
    print(json.dumps(results, indent=4))
    #print(results)