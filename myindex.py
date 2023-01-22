from dash import html, dcc
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dash_table
import plotly.graph_objects as go

from app import *
from globals import * 

# ===== TRATAMENTO DOS DADOS ===== # 
df = pd.read_csv('100_anime.csv')

df = df.sort_values('Rating', ascending=False)
df = df.drop_duplicates(subset='Name')

df_ano = df.groupby('Rating')

trace = df.groupby('Rating')['Name'].sum().tail(10).reset_index()
fig = px.bar(df, x=trace['Rating'].unique(), y=trace['Name'].unique())
fig.update_layout(height=340, xaxis={'title': None}, yaxis={'title': None})

trace_piores = df.groupby('Rating')['Name'].sum().head(10).reset_index()
fig2 = px.bar(df, x=trace_piores['Rating'].unique(), y=trace_piores['Name'].unique())
fig2.update_layout(height=340, xaxis={'title': None}, yaxis={'title': None})

# =========  Layout  =========== #
app.layout = dbc.Container([
    dbc.Row([ 
        dbc.Col([ 
            dbc.Col([
        dbc.Card([
                html.H1('100 Animações', style={'color':'#678983'}),
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
                        dbc.ModalBody("https://www.imdb.com/list/ls057577566/", style={'font-size':'20px'}),
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
                    dbc.Tabs([
                        dcc.Tab(label='Melhores Avaliações', children=[
                            dcc.Graph(id='graph2', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig),
                            dbc.Button("Visualizar Grágico", id="open4", n_clicks=0, style={'border':'none', 'border-radius':'5px', 'width':'95%', 'margin-left':'10px', 'margin-top':'5px', 'margin-bottom':'10px', 'background-color':'#678983', 'color':'black'}),
                            dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Melhores Avaliações:")),
                                dbc.ModalBody(dcc.Graph(id='graph02', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig)),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fechar", id="close4", className="ms-auto", n_clicks=0, style={'border-radius':'5px'}
                                    )
                                ),
                            ],
                            id="modal4",
                            size="xl",
                            is_open=False,
                        ),
                        ], style={'color':'white', 'background-color':'#181D3135'}),

                        dcc.Tab(label='Piores Avaliações', children=[
                            dcc.Graph(id='graph5', className='dbc', config={"displayModeBar": False, "showTips": False}, animate=True, figure=fig2),
                            dbc.Button("Visualizar Gráfico", id="open3", n_clicks=0, style={'border':'none', 'border-radius':'5px', 'width':'95%', 'margin-left':'20px', 'margin-top':'5px', 'margin-bottom':'10px', 'background-color':'#678983', 'color':'black'}),
                        ]),
                        dbc.Modal([
                            dbc.ModalHeader(dbc.ModalTitle("Piores Avaliações:")),
                            dbc.ModalBody(dcc.Graph(id='graph05', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig2)),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "Fechar", id="close3", className="ms-auto", n_clicks=0, style={'border-radius':'5px'}
                                )
                            ),
                        ],
                        id="modal3",
                        size="xl",
                        is_open=False,
                    ),
                    ], style={'color':'white', 'background-color':'#181D3135'})
                ], style={'margin-top': '15px', 'margin-left': '10px'}),
        ], width=12),
        ]), 
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.Legend('DATASET UTILIZADO', style={'text-align':'center'}),
                    dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns],
                    style_header={ 'border': '1px solid #EAEAEA', 'background-color':'#678983', 'color':'black', 'text-align':'center'},
                    filter_action='native',
                    style_cell={ 'border': '1px solid #EAEAEA', 'textAlign': 'left'},
                    page_size=2,     
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto', 'color':'white', 'background-color':'transparent'
                    }, id='tableData')
                    ], style={'color':'white', 'background-color':'#181D3135'})
                ], style={'margin-top': '10px', 'margin-left':'10px'}, width=8),
                dbc.Col([ 
                    dbc.Card([ 
                        html.H1('Site usado:'),
                        html.Img(src='./assets/img-site.png'),
                    ], style={'margin-top':'50px', 'margin-left':'20px'})
                ], width=3)
            ]),
        ]),
      ], md=10)
   ])
 ], fluid=True)



# =========  Callbacks  =========== #
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal2", "is_open"),
    [Input("open2", "n_clicks"), Input("close2", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal5", "is_open"),
    [Input("open5", "n_clicks"), Input("close5", "n_clicks")],
    [State("modal5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal4", "is_open"),
    [Input("open4", "n_clicks"), Input("close4", "n_clicks")],
    [State("modal4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal3", "is_open"),
    [Input("open3", "n_clicks"), Input("close3", "n_clicks")],
    [State("modal3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)