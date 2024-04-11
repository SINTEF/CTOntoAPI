import dash_bootstrap_components as dbc
from dash import html, dcc
from frontend.viz_graph import graph_layout

import uuid


def get_layout():
    """
    Layout of the left sidebar. Contains global information and stats as well as some settings
    :return:
    """

    return html.Div(
        id="main-column-container",

        children=[
            dbc.Card(
                style={"height": "100%"},
                children=[

                    dbc.CardHeader(
                        id="viz-graph-container-card",
                        children=[
                            html.Div("Node Details"),
                        ],
                    ),
                    dbc.CardBody(
                        html.Div(
                            id="viz-graph-card-body",
                            style={"height": "100%"},
                            children=[
                                dbc.InputGroup(
                                    style={"margin-bottom": "10px"},
                                    children=[dbc.InputGroupText("URI"),
                                              dbc.Input(
                                        id="node-uri", type="text", debounce=True, placeholder=""),
                                        dbc.Button("Fetch", id="fetch-button", color="primary", n_clicks=0),],


                                ),
                                # tables of node details, hide by default
                                html.Div(
                                    id="node-details",
                                    style={"display": "none"},
                                    children=[
                                        # html.Hr(),
                                        # html.H6("Data Properties"),
                                        html.Div(
                                            id="node-details-table-container",
                                            style={"overflow": "scroll", "height": "30vh"},
                                            children=[
                                                dcc.Tabs(
                                                    id="node-details-tabs",
                                                    value="node-details-tab",
                                                    children=[
                                                        dcc.Tab(label="",
                                                                id="node-details-tab",
                                                                value="node-details-tab",

                                                                children=[
                                                                    html.Div(
                                                                        id="node-details-table-div",
                                                                        style={
                                                                            "overflow": "scroll", "max-height": "20vh"},
                                                                        children=[dbc.Table(
                                                                            id="node-details-table", striped=True, bordered=True, hover=True,

                                                                        ),]
                                                                    ),


                                                                ]),
                                                        dcc.Tab(label="",
                                                                id="altnode-details-tab",
                                                                value="altnode-details-tab",
                                                                style={
                                                                    "display": "none"},
                                                                children=[
                                                                    html.Div(
                                                                        id="altnode-details-table-div",
                                                                        style={
                                                                            "overflow": "scroll", "max-height": "20vh"},
                                                                        children=[
                                                                            dbc.Table(
                                                                                id="altnode-details-table", striped=True, bordered=True, hover=True,

                                                                            ),
                                                                        ]),

                                                                ]),

                                                    ]
                                                )
                                            ]
                                        ),
                                        graph_layout.get_layout(),
                                    ],
                                    
                                ),
                                # graph_layout.get_layout(),
                            ]
                        )
                    ),

                ],

            ),

        ],
    )
