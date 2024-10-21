import json
from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
)

from util.client_api import ClientAPI

lamp_api = ClientAPI(get_environment_variable("LAMPAPI"))
lamp_api_token = get_environment_variable("LAMPAPI_TOKEN")

                                          
def entity_retrival(term: str) -> list:
    lookup_result = lamp_api.get_json(
        "/lookup/entity-retrieval",
        name=term,
        token=lamp_api_token,
        kg="wikidata",
        retries=3,
    )

    return_values = []

    if lookup_result:
        #for values in lookup_result.values():
        #    for entity in values:
        for entity in lookup_result:
                #if entity["name"] == term:
                if "id" in entity:
                    id = entity["id"]
                    if "name" in entity:
                        name = entity["name"]
                    else:
                        name = ""
                    if "description" in entity:
                        description = entity["description"]
                    else:
                        description = ""
                    if "cosine_similarity" in entity:
                        cosine_similarity = entity["cosine_similarity"]
                    elif "jaccardNgram_score" in entity:
                        cosine_similarity = entity["jaccardNgram_score"]
                    elif "jaccard_score" in entity:
                        cosine_similarity = entity["jaccard_score"]
                    elif "ed_score" in entity:
                        cosine_similarity = entity["ed_score"]
                    elif "es_score" in entity:
                        cosine_similarity = entity["es_score"]
                    else:
                        cosine_similarity = 0.0
                
                    return_values.append({"uri": id, "name" : name, "description": description, "score": cosine_similarity})
    
    return_values_sorted = sorted(return_values, key=lambda x: x["score"], reverse=True)
    #remove values with score less than 0.5
    return_values = [x for x in return_values_sorted if x["score"] > 0.5]

    #if return_values is empty, return first 10 results
    if not return_values or len(return_values) == 0:
        return_values = return_values_sorted[:20]
    
    return return_values


def get_labels(uri: str) -> list:
    data = {"json": [uri]}
    #print(data)

    lookup_result = lamp_api.post(
        "/entity/labels",
        id=uri,
        token=lamp_api_token,
        kg="wikidata",
        json=data,
        retries=3,
    )

    #print(lookup_result)
    #convert lookup_result to json
    


    return_values = []

    if lookup_result:
#        lookup_result = json.loads(lookup_result)
#        if "wikidata" in lookup_result:
#            wikidata = lookup_result["wikidata"]
#            if uri in wikidata:
        wikidata = json.loads(lookup_result)
        if uri in wikidata:
                data_uri = wikidata[uri]
                if "description" in data_uri:
                    description = data_uri["description"]
                    return_values.append({"description": description})
                if "url" in data_uri:
                    url = data_uri["url"]
                    return_values.append({"url": url})
                if "labels" in data_uri:
                    labels = data_uri["labels"]
                    for key, value in labels.items():
                        return_values.append({key: value})
    
    return return_values