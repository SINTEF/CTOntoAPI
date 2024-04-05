from datetime import datetime
from dash.dependencies import Input, Output, State
from dash import dcc, ctx
from frontend.app import app
from util.log import logger



logger.info("Initializing navbar callbacks...")


@app.callback(
    Output("help-offcanvas", "is_open"),
    Input("help-button", "n_clicks"),
    [State("help-offcanvas", "is_open")],
    prevent_initial_call=True,
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open









