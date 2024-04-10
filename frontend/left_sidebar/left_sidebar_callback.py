import time
from util.log import logger
from frontend.app import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import no_update, ctx, dash_table
from frontend.app import backend_api
import pandas as pd


logger.info("Initializing left sidebar callbacks...")
#disable search button until search is complete
@app.callback(
    Output("search-button", "disabled", allow_duplicate=True),
    Input("search-button", "n_clicks"),
    Input("search-term", "value"),
    prevent_initial_call=True,
)
def disable_search_button(n_clicks, search_term):
    logger.info("disable_search_button")
    triggered_id = ctx.triggered_id

    if n_clicks or triggered_id == "search-term":
        return True
    return no_update

@app.callback(
    Output("search-button", "n_clicks"),
    Input("search-term", "value"),
    State("search-button", "n_clicks"),
    State("search-button", "disabled"),
    prevent_initial_call=True,
)
def simulate_search_button(search_term, n_clicks, disabled):
    logger.info("simulate_search_button")
    triggered_id = ctx.triggered_id

    if not disabled:
        return n_clicks + 1
    
    return no_update

#dash callback function for search button
@app.callback(
    Output("search-result-list", "children"),
    Output("search-result", "style"),
    Output("search-button", "disabled"),
    Input("search-button", "n_clicks"),
    State("search-term", "value"),
    State("search-graph", "value"),
    prevent_initial_call=True,
    
) 
def search_concept(n_clicks, search_term, search_graph):
    logger.info("search_concept")
    triggered_id = ctx.triggered_id
    #print(search_term)
    #print(search_graph)

    #disable the search button and enable again after search
    #
    style = {"display": "block"}
    if n_clicks: #or triggered_id == "search-term":
        #time.sleep(10)
        logger.info(f"""Search term: {search_term} in graph {search_graph}""")
        ###Call the search function get /search/{search_term}
        #params = {"term": search_term}
        if search_graph == "wikidata":
            concepts = backend_api.get_json(f"/wikidata/search", retries=5, term=search_term.strip())
        else:
            concepts = backend_api.get_json(f"/search", retries=5, term=search_term.strip())
        #print(concepts)
        #create a table with two columns: uri and score, the values are from the concepts
        if concepts:
            #Concepts is a list of dictionaries with uri and score
            concepts_df = pd.DataFrame(concepts)
            #table = dbc.Table.from_dataframe(concepts_df, striped=True, bordered=True, hover=True)
            table = dash_table.DataTable(
                id='search-result-table',
                columns=[{"name": i, "id": i} for i in concepts_df.columns],
                data=concepts_df.to_dict('records'),
                style_table={'overflowX': 'auto', 'overflowY': 'auto', 'max-height': '60vh'},
                style_cell={'textAlign': 'left'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ]
            )
            return table, style, False
        
    return None, {"display": "none"}, False
    
    

    
   
#callback function when one cell in the search result table is clicked
@app.callback(
    Output("node-uri", "value"),
    Input("search-result-table", "active_cell"),
    State("search-result-table", "data"),
    prevent_initial_call=True,
)
def on_click_table(active_cell, data):
    if active_cell:
        row = active_cell["row"]
        #print(data[row])
        if data[row] and "uri" in data[row]:
            return data[row]["uri"]
        #print(row)
        #print(data)
        #print(active_cell)
        
    return no_update