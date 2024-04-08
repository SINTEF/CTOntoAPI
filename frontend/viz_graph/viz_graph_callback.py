import time
from util.log import logger
from frontend.app import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import no_update, ctx, dash_table
from frontend.client.client_api import get_json
import pandas as pd

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
    Output("node-details", "style"),
    Output("fetch-button", "disabled"),
    Input("fetch-button", "n_clicks"),
    State("node-uri", "value"),
    prevent_initial_call=True,

)
def fetch_node_details(n_clicks, node_uri):
    logger.info("fetch_node_details")
    style = {"display": "block", "overflow": "scroll", "height": "500px"}

    # print(node_uri)

    # disable the fetch button and enable again after fetch
    if n_clicks:
        # time.sleep(3)
        # call the client api to fetch the node details at /data_properties
        node_details = get_json(f"/data_properties", retries=3, uri=node_uri.strip())
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

        time.sleep(0.1)
        return table.children, style, False
    
    time.sleep(0.1)
    return None, {"display": "none"}, False

    #return no_update, no_update, no_update
    
    #return no_update, no_update