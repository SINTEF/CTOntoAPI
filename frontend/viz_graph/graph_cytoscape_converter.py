from util.log import logger
from util.prefix_mapper import convert_uri_to_label


def _create_cytoscape_node(node):
    return {
        "data": {
            "id": node["uri"],
            "label": node["label"],
            "uri": node["uri"],
        }
    }

def _create_cytoscape_relationship(iri_from, iri_to, label = ""):
    return {
        "data": {
            "source": iri_from,
            "target": iri_to,
            "label": label
        }
    }




def convert_to_cytoscape(root_node_iri: str, edges):
    cytoscape_elements = []
    nodes = set()
    nodes.add(root_node_iri)

    # Create the outgoing edges
    for edge in edges["outgoing"]:
        nodes.add(edge["object"])
        cytoscape_elements.append(_create_cytoscape_relationship(root_node_iri, edge["object"], convert_uri_to_label(edge["property"])))

    # Create the incoming edges
    for edge in edges["incoming"]:
        nodes.add(edge["subject"])
        cytoscape_elements.append(_create_cytoscape_relationship(edge["subject"], root_node_iri, convert_uri_to_label(edge["property"])))

    # Create the nodes
    for node in nodes:
        cytoscape_elements.append(_create_cytoscape_node({"uri": node, "label": convert_uri_to_label(node)}))

    return cytoscape_elements

