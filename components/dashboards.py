# ===== IMPORTAÇÕES ==== #
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table
import plotly.express as px
import plotly.graph_objects as go
from globals import * 
from app import app 

# ===== TRATAMENTO DOS DADOS ==== # 


# =========  LAYOUT  =========== #
layout = dbc.Col([
       dbc.Row([
        dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph1')
                ], style={'margin-top': '15px', 'margin-left': '10px'}),
        ]),
    ]), 
       dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph2')
                    ], style={'color':'white', 'background-color':'#181D3135'})
                ], style={'margin-top': '10px', 'margin-left':'10px'})
        ]),
        dbc.Col([
            dbc.Card([
                dcc.Graph(id='graph3')
            ], style={'margin-top': '10px'})
        ])
    ]),

# =========  Callbacks  =========== #
