from dash import html
import dash_bootstrap_components as dbc

# from frontend.factory_graph import factory_graph_layout
from frontend.navbar import navbar_layout
from frontend.left_sidebar import left_sidebar_layout
from frontend.viz_graph import viz_graph_layout
from frontend.app import app

from util.log import logger


def get_layout():
    """
    Main page layout
    :return:
    """
    return html.Div(
        id="full-page-container",
        children=[
            # Navbar:
            navbar_layout.get_layout(),
            # Body:
            dbc.Card(
                style={"flex": 1},
                id="content-card",
                children=[
                    dbc.CardBody(
                        [
                            html.Div(
                                children=[
                                    dbc.Row(
                                        style={"width": "100%"},
                                        children=
                                        [
                                            dbc.Col(
                                                left_sidebar_layout.get_layout(), width=4),
                                            dbc.Col(
                                                [
                                                    viz_graph_layout.get_layout(),
                                                ],
                                                width=8,
                                            ),
                                        ]
                                    )


                                    # factory_graph_layout.get_layout(),

                                ],
                                id="content-rows-container",
                            ),
                        ],
                        id="main-card-body",
                    )
                ],
            ),

            dbc.Navbar(
                id="publication-info-container",
                children=[

                    # add logo sintef_white.png here
                    html.A(
                        html.Img(
                            src=app.get_asset_url("sintef_white.png"),
                            height="32px",
                        ),
                        href="https://www.sintef.no/",
                    ),

                    html.Div(
                        id="publication-date-container",
                        className="publication-info-subcontainer",
                        children=[
                            html.Div(
                                "Publication date:",
                                className="publication-info-key",
                            ),
                        ],
                    ),
                    html.Div(
                        id="license-container",
                        className="publication-info-subcontainer",
                        children=[
                            html.Div(
                                "License:",
                                className="publication-info-key",
                            ),
                            html.Div(
                                id="license-text-container",
                                children=[
                                    # "This work and the data is restricted by the ",
                                    html.A(
                                        "Creative Commons Attribition Non Commercial Share Alike 4.0 International license",
                                        href="https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
                                    ),
                                    # ".",
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="github-link-container",
                        className="publication-info-subcontainer",
                        children=[
                            html.Div(
                                "Source code:",
                                className="publication-info-key",
                            ),
                            html.A(
                                "https://github.com/Circular-TwAIn/CircularTwAIn-Ontology-Library",
                                href="https://github.com/Circular-TwAIn/CircularTwAIn-Ontology-Library",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
