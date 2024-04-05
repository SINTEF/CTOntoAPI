from dash import html, dcc
import dash_bootstrap_components as dbc
from frontend.app import app
from util.log import logger

def get_layout():
    """
    Layout of the navbar
    :return:
    """
    return dbc.Navbar(
        children=[
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                # src=app.get_asset_url("sintef_white.png"),
                                src=app.get_asset_url("Circular Twain Logo-black.svg"),
                                height="64px",
                            )
                        ),
                    ],
                    align="center",
                ),
                href="https://www.circular-twain-project.eu",
            ),
            html.Div(
                [
                    dbc.NavbarBrand(
                        "CircularTwAIn Ontology Library",
                        className="navbar-brand",
                        #set the text to bold, color red
                        style={"font-weight": "bold"},
                    ),
                ],
                style={"flex": 1},
            ),
            html.Div(
                [
                    dbc.Button(
                        [html.I(className="bi bi-info-circle-fill me-2"), "Help"],
                        id="help-button",
                        n_clicks=0,
                        color="primary",
                        size="sm",
                        style={"border": "none"},
                    ),
                ]
            ),
            dbc.Offcanvas(
                [
                    html.P(
                        [
                            html.Div(
                                "Graph and Interaction:", style={"font-weight": "bold"}
                            ),
                            html.Div(
                                "To be updated.",
                                style={"padding-bottom": "5px"},
                            ),
                            html.Div(
                                "To be updated."
                            ),
                        ]
                    ),
                ],
                id="help-offcanvas",
                title="Information and Help",
                is_open=False,
            ),
        ],
    )
