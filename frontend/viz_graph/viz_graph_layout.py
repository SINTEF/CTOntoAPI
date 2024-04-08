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
                            ]
                        )
                    ),

                ],

            )
        ],
    )
