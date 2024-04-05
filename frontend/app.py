import logging
import dash
#from django_plotly_dash.util import static_asset_path
from flask import Flask
import dash_bootstrap_components as dbc

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
    assets_folder="./assets",
    update_title=None,
    title="CircularTwAIn Ontology Library",
    server=server,

)

app._favicon = "favicon.png"



