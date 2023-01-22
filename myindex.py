from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import sidebar, dashboards
from app import *

# =========  Layout  =========== #
app.layout = dbc.Container([
    dbc.Row([ 
        dbc.Col([ 
            dbc.Col([
        dbc.Card([
                html.H1('100 Animes', style={'color':'#678983'}),
                html.P('Trabalho final', style={'color':'white', 'letter-spacing':'2px', 'font-weight':'400', 'font-size':'20px'}),
                html.Hr(),

        #Seção perfil
                dbc.Button(id='botao_avatar',
                children=[html.Img(src='/assets/animes.webp', id='avatar_change', alt='Avatar', className='perfil_avatar', style={'border-radius':'15px'})], 
                style={'background-color':'transparent', 'border-color':'transparent'}),
                html.Button('Código', className='button-git', id="open2", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Link do código:", style={'font-weight':'bold'})),
                        dbc.ModalBody("https://github.com/MariaE-duarda/DiscTopDash", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close2", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px', 'background-color':'transparent', 'border': '1px solid #678983'}
                        )),
                ],
                id="modal2",
                size="lg",
                is_open=False,
                ),
                html.Button('Informações', className='button-git', id="open", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Informações:", style={'font-weight':'bold'})),
                        dbc.ModalBody("Projeto final da disciplina de Tópicos Especiais de Informática. \nRaspagem de dados e criação de dashboard com os dados extraidos.", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px', 'background-color':'transparent', 'border': '1px solid #678983'}
                        )),
                ],
                id="modal",
                size="lg",
                is_open=False,
                ),
                html.Button('Site usado',className='button-git', id="open5", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Link do site usado:", style={'font-weight':'bold'})),
                        dbc.ModalBody("https://m.imdb.com/feature/genre/?ref_=nv_ch_gr", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close5", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px', 'background-color':'transparent', 'border': '1px solid #678983'}
                        )),
                ],
                id="modal5",
                size="lg",
                is_open=False,
                ),

        ], id='sidebar_completa', style={'margin-top':'15px', 'text-align':'center'}),
        ])
        ], md=2), 
        dbc.Col([ 
            dbc.Col([
       dbc.Row([
        dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph1')
                ], style={'margin-top': '15px', 'margin-left': '10px'}),
        ], width=6),
        dbc.Col([ 
            dbc.Card([ 
                dcc.Graph(id='graph2')
            ], style={'margin-top':'10px'})
        ], width=6)
        ]), 
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph3')
                    ], style={'color':'white', 'background-color':'#181D3135'})
                ], style={'margin-top': '10px', 'margin-left':'10px'})
        ]),
        ]),
      ], md=10)
   ])
 ], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)