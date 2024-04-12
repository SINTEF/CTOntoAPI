import logging
import dash
#from django_plotly_dash.util import static_asset_path
from flask import Flask
import dash_bootstrap_components as dbc
from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
)

from util.client_api import ClientAPI

## Diskcache
""" import diskcache
from dash import DiskcacheManager
cache = diskcache.Cache("./cache")
callback_manager = DiskcacheManager(cache) """
####

"""
Plotly dash app instance.
Separated from presentation.py to avoid circular dependencies with callback files importing the "app" instance. 
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Build App
external_stylesheets = [dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP]
server = Flask(__name__)
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    assets_folder="../assets",
    update_title=None,
    title="CircularTwAIn Ontology Library",
    server=server,
    #background_callback_manager=callback_manager,

)

FAST_API_HOST = get_environment_variable("FAST_API_HOST")
FAST_API_PORT = get_environment_variable_int("FAST_API_PORT")
API_URI = f"http://{FAST_API_HOST}:{FAST_API_PORT}"
backend_api = ClientAPI(API_URI)

app._favicon = "favicon.png"



