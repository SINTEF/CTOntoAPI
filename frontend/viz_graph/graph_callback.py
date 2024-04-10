import time
from frontend.viz_graph.graph_cytoscape_converter import convert_to_cytoscape
from util.log import logger
from frontend.app import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import no_update, ctx, dash_table

import pandas as pd
from frontend.app import backend_api

logger.info("Initializing cyto graph callbacks...")


#update cytoscape-graph
@app.callback(
    Output("cytoscape-graph", "elements"),
    Output("kg-container", "style"),
    Input("fetch-button", "n_clicks"),
    State("node-uri", "value"),
    State("search-graph", "value"),
    prevent_initial_call=True,
)
def update_graph(n_clicks, node_uri, search_graph):
    logger.info("fetch_node_details")
    triggered_id = ctx.triggered_id

    if not node_uri:
        return [{"data": {"id": "empty", "label": "No data available"}}], {"display": "none"}

    if search_graph == "circulartwain":
        edges = backend_api.get_json("/object_properties", retries=5, uri=node_uri)
        #print(edges)
        if edges:
            graph_elements = convert_to_cytoscape(node_uri, edges)
            #print(graph_elements)
            return graph_elements, {"display": "block"}
    
    return [{"data": {"id": "empty", "label": "No data available"}}], {"display": "none"}

#tapnode
@app.callback(
    Output("altnode-details-table", "children"),
    Output("altnode-details-tab", "label"),
    Output("node-details-tabs", "value", allow_duplicate=True),
    Output("altnode-details-tab", "style", allow_duplicate=True),
    Input("cytoscape-graph", "tapNode"),
    State("node-uri", "value"),
    prevent_initial_call=True,
)
def tap_node(node, root_node):
    logger.info("tap_node")

    if node:
        node_uri = node["data"]["id"]
        node_label = node["data"]["label"]

        if node_uri.strip() == root_node.strip():
            tab_value = "node-details-tab"
            return no_update, no_update, tab_value, no_update

        node_details = backend_api.get_json(f"/data_properties", retries=3, uri=node_uri.strip())

        #tab_label = node_label
        tab_value = "altnode-details-tab"
        tab_style = {"display": "block"}


         # Initialize lists to store keys and values
        keys = ["uri"]
        values = [node_uri]

        # Extract keys and values from the JSON input
        for entry in node_details:
            for key, value in entry.items():
                keys.append(key)
                values.append(value)

        # Create DataFrame
        df = pd.DataFrame({'Data Property': keys, 'Value': values})

        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        return table.children, node_label, tab_value, tab_style

    return no_update    