import dash_bootstrap_components as dbc
from dash import html


def get_layout():
    """
    Layout of the left sidebar. Contains global information and stats as well as some settings
    :return:
    """

    return html.Div(
        id="left-sidebar-container",
        children=[
            dbc.Card(
                style={"height": "100%"},
                children=[

                    dbc.CardHeader(
                        id="left-sidebar-container-card",
                        children=[
                            html.Div("Vocabulary Search"),
                        ],
                    ),
                    dbc.CardBody(
                        html.Div(
                            id="search-container",
                            style={"height": "100%"},
                            children=[
                                # dcc.Store(id="store-search-term", data=""),
                                dbc.InputGroup(

                                    [dbc.InputGroupText(
                                        "Knowledge Graph", style={"width": "150px"}),
                                        dbc.Select(
                                        id="search-graph",

                                        options=[

                                            {"label": "CircularTwAIn Ontology Library",
                                                "value": "circulartwain"},
                                            {"label": "Wikidata",
                                             "value": "wikidata"},
                                        ],
                                        value="circulartwain",
                                    )
                                    ],
                                    # adjust the space between the two InputGroup
                                    style={"margin-bottom": "5px"},

                                ),

                                dbc.InputGroup(
                                    [dbc.InputGroupText(
                                        "Search Term", style={"width": "150px"}), dbc.Input(id="search-term", type="text", debounce=True, placeholder="Enter search term...")],

                                ),

                                # Search button
                                dbc.Button("Search", id="search-button", n_clicks=0,
                                           style={"width": "100%", "margin-top": "5px"}),

                                # Search result, hide by default
                                html.Div(
                                    id="search-result",
                                    style={"display": "none"},
                                    children=[
                                        html.Hr(),
                                        html.H6("Search Result"),
                                        html.Div(
                                            id="search-result-list",
                                            # children=[
                                            #     dbc.Table(
                                            #         striped=True,
                                            #         bordered=True,
                                            #         hover=True,
                                            #         id="search-result-table",
                                            #     )
                                            # ],
                                        ),
                                        html.Div(id ="search-button-trigger-id", style={"display": "none"}, children=0)
                                    ],
                                ),

                            ]
                        )
                    ),

                ],

            )
        ],
    )
