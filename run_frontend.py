import os
from frontend.app import app
from frontend import page_layout
from frontend.navbar import navbar_callback
from frontend.left_sidebar import left_sidebar_callback
from frontend.viz_graph import viz_graph_callback
from frontend.viz_graph import graph_callback

from enum import Enum
from dash import html, ctx, no_update
from dash.dependencies import Input, Output, State

from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc

from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
)

from util.log import logger

if __name__ == "__main__":
    server = app.server
    # Initialize layout

    logger.info("Initializing app layout...")
    app.layout = page_layout.get_layout
    logger.info("Finished initializing the app layout.")


    logger.info(f"Starting the frontend")




    #app.scripts.append_script({"external_url": ["https://apis.google.com/js/api.js"]})

    app.run(
        host=get_environment_variable("FRONTEND_HOST"),
        debug=False,
        port=get_environment_variable_int("FRONTEND_PORT"),
        use_reloader=False,
    )

