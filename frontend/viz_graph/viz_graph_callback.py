import time
from util.log import logger
from frontend.app import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import no_update, ctx, dash_table
from util.prefix_mapper import convert_uri_to_label

import pandas as pd
from frontend.app import backend_api

logger.info("Initializing viz graph callbacks...")

# disable fetch button until fetch is complete


@app.callback(
    Output("fetch-button", "disabled", allow_duplicate=True),
    Input("fetch-button", "n_clicks"),
    Input("node-uri", "value"),
    prevent_initial_call=True,
)
def disable_fetch_button(n_clicks, node_uri):
    logger.info("disable_fetch_button")
    triggered_id = ctx.triggered_id

    if n_clicks or triggered_id == "node-uri":
        return True
    return no_update


@app.callback(
    Output("fetch-button", "n_clicks"),
    Input("node-uri", "value"),
    State("fetch-button", "n_clicks"),
    State("fetch-button", "disabled"),
    prevent_initial_call=True,
)
def simulate_fetch_button(node_uri, n_clicks, disabled):
    logger.info("simulate_fetch_button")
    triggered_id = ctx.triggered_id

    if not disabled:
        return n_clicks + 1

    return no_update

# dash callback function for fetch button


@app.callback(
    Output("node-details-table", "children"),
    Output("node-details-tab", "label"),
    Output("node-details-tabs", "value"),
    Output("node-details", "style"),
    Output("altnode-details-tab", "style"),
    Output("fetch-button", "disabled"),
    Input("fetch-button", "n_clicks"),
    State("node-uri", "value"),
    State("search-graph", "value"),
    prevent_initial_call=True,

)
def fetch_node_details(n_clicks, node_uri, search_graph):
    logger.info("fetch_node_details")
    container_style = {"display": "block", "height": "400px"} #"overflow": "scroll", "max-height": "300px"}
    altnode_style = {"display": "none"}
    #table_style = {"overflow": "scroll", "max-height": "300px"}
    # print(node_uri)

    # disable the fetch button and enable again after fetch
    if n_clicks:
        # time.sleep(3)
        # call the client api to fetch the node details at /data_properties
        if search_graph == "wikidata":
            node_details = backend_api.get_json(f"/wikidata/labels", retries=3, uri=node_uri.strip())
        else:
            node_details = backend_api.get_json(f"/data_properties", retries=3, uri=node_uri.strip())
        #print(node_details)


        # Initialize lists to store keys and values
        keys = []
        values = []

        # Extract keys and values from the JSON input
        for entry in node_details:
            for key, value in entry.items():
                keys.append(key)
                values.append(value)

        # Create DataFrame
        df = pd.DataFrame({'Data Property': keys, 'Value': values})

        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        tab_label = convert_uri_to_label(node_uri)
        tab_value = "node-details-tab"

        time.sleep(0.1)
        return table.children, tab_label, tab_value, container_style, altnode_style, False
    
    time.sleep(0.1)
    return None, "", no_update, {"display": "none"}, no_update, False

    #return no_update, no_update, no_update
    
    #return no_update, no_update