import dash_bootstrap_components as dbc
from dash import html, dcc

import uuid

def get_layout():
    """
    Layout of the left sidebar. Contains global information and stats as well as some settings
    :return:
    """


    return html.Div(
        id="left-sidebar-container",
        children=[
            dbc.Card(
                [
                    dbc.CardHeader(
                        id="global-information-container-card",
                        children=[
                            html.Div("ChatBot"),
                        ],
                    ),
                    dbc.CardBody(
                        html.Div(
                            id="chatbot-container",
                            children=[
                                dcc.Store(id="store-conversation", data=""),
                                
                                dcc.Interval(
                                    id="interval-update-chatbot",
                                    interval=500,
                                    n_intervals=0,
                                ),
                                html.Div(
                                    style={
                                        "width": "100%",
                                        #"max-width": "100%",
                                        #"height": "75vh",
                                        "height": "100%",
                                        "margin": "auto",
                                        "overflow-y": "auto",
                                        "display": "flex",
                                        "flex-direction": "column",
                                    },
                                    id="display-conversation",
                                ),
                            ]
                        )
                    ),
                    dbc.InputGroup(
                        style={"width": "80%", "margin": "auto", "margin-bottom": "5px"},
                        children=[
                            dbc.Input(id="user-input", placeholder="Write to the chatbot...", type="text",
                                      debounce=True),
                            # dbc.Button("Submit", id="submit", n_clicks=0),
                            dbc.Button("record-done", id="record-done-button", n_clicks=0, style=dict(display='none')),
                            dbc.Button("stt-done", id="stt-done-button", n_clicks=0,
                                       style=dict(display='none')),
                            dbc.Button(
                                [html.I(className="bi bi-mic")],
                                id="talk-button",
                                n_clicks=0,
                                size="sm",
                                color="success",
                                active=False
                            )
                        ],
                    ),
                ],
                #style={"margin-bottom": "1rem"},
            )
        ],
    )
