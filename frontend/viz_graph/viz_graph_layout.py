import dash_bootstrap_components as dbc
from dash import html, dcc

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
                            children=[
                                dbc.InputGroup(
                                    [dbc.InputGroupText("URI"),
                                        dbc.Input(
                                            id="node-uri", type="text", debounce=True, placeholder=""),
                                        dbc.Button("Fetch", id="fetch-button", color="primary", n_clicks=0),],


                                ),
                                # tables of node details, hide by default
                                html.Div(
                                    id="node-details",
                                    children=[
                                        html.Hr(),
                                        # html.H6("Data Properties"),
                                        html.Div(
                                            id="node-details-table-container",
                                            children=[
                                                dbc.Table(
                                                    id="node-details-table", striped=True, bordered=True, hover=True)
                                            ]
                                        )

                                    ],
                                    style={"display": "none"}
                                ),
                            ]
                        )
                    ),

                ],

            )
        ],
    )
