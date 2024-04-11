from dash import html, dcc
import dash_bootstrap_components as dbc
from frontend.app import app
from util.log import logger
from frontend import resources_manager
import dash_cytoscape as cyto

# Load extra layouts
cyto.load_extra_layouts()

CY_GRAPH_STYLE_STATIC = resources_manager.load_json(
    "cytoscape-graph-style.json")


def get_layout():
    return html.Div(
        id="kg-container",
        #style={"height": "100%", "overflow": "scroll"},
        #style={"display": "none"},
        children=[
            dcc.Loading(
                className="kg-loading-indicator-container",
                id="kg-loading-indicator-container",
                type="dot",
                color="#446e9b",
                children=[
                    cyto.Cytoscape(
                        id="cytoscape-graph",
                        #layout={"name": "cose"},
                        layout={"name": "klay"},
                        #layout={"name": "dagre"},
                        style={
                            "width": "100%",
                            #"height": "300px",
                            "height": "100%",
                            #"overflow": "scroll",
                        },
                        #wheelSensitivity=0.1,
                        minZoom=0.5,
                        maxZoom=4,
                        #zoom=2,
                        responsive=False,
                        stylesheet=CY_GRAPH_STYLE_STATIC,
                        className="factory-graph",
                    ),
                ],
            )
        ],
    )
