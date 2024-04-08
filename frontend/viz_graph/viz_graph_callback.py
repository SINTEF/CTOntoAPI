from util.log import logger
from frontend.app import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import no_update, ctx, dash_table
from frontend.client.client_api import get_json
import pandas as pd

logger.info("Initializing viz graph callbacks...")